#!/usr/bin/env python3
"""Audit an internal timeline; no network, model or media dependencies."""
import argparse
import json
import math
from pathlib import Path
import re
import sys

EPS = 1e-6
WORD = re.compile(r"[A-Za-z]+(?:['’][A-Za-z]+)*")


def audit(data):
    issues = []

    def issue(code, message):
        issues.append({"code": code, "message": message})

    def number(value, label):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError(f"{label} must be a finite number")
        return float(value)

    if not isinstance(data, dict):
        raise ValueError("root must be an object")
    duration = number(data.get("duration"), "duration")
    if duration <= 0:
        raise ValueError("duration must be positive")
    segments = data.get("segments")
    if not isinstance(segments, list) or not segments:
        raise ValueError("segments must be a nonempty list")
    previous = 0.0
    for i, segment in enumerate(segments):
        if not isinstance(segment, dict):
            raise ValueError(f"segment {i + 1} must be an object")
        start = number(segment.get("start"), f"segment {i + 1}.start")
        end = number(segment.get("end"), f"segment {i + 1}.end")
        if abs(start - previous) > EPS:
            issue("coverage", f"segment {i + 1} starts at {start:g}, expected {previous:g}")
        if start < 0 or end <= start or end > duration + EPS:
            issue("segment_range", f"segment {i + 1} has invalid interval {start:g}–{end:g}")
        previous = end
    if abs(previous - duration) > EPS:
        issue("total", f"timeline ends at {previous:g}, declared duration is {duration:g}")

    speech = data.get("speech", [])
    if not isinstance(speech, list):
        raise ValueError("speech must be a list")
    parsed, estimates = [], []
    for i, line in enumerate(speech):
        if not isinstance(line, dict):
            raise ValueError(f"speech {i + 1} must be an object")
        start = number(line.get("start"), f"speech {i + 1}.start")
        end = number(line.get("end"), f"speech {i + 1}.end")
        speaker, text = line.get("speaker"), line.get("text")
        language = line.get("language", "en")
        overlap = line.get("overlap", False)
        if not isinstance(speaker, str) or not speaker.strip() or not isinstance(text, str) or not text.strip():
            raise ValueError(f"speech {i + 1} needs a speaker and nonempty text")
        if not isinstance(language, str) or not isinstance(overlap, bool):
            raise ValueError(f"speech {i + 1} has invalid language/overlap")
        if start < 0 or end <= start or end > duration + EPS:
            issue("speech_range", f"speech {i + 1} lies outside the timeline or has no time")
        if language.lower().split("-")[0] == "en" and end > start:
            rate = number(line.get("words_per_second", 2.4), f"speech {i + 1}.words_per_second")
            if rate <= 0:
                raise ValueError("words_per_second must be positive")
            words = len(WORD.findall(text))
            needed = words / rate
            if not words:
                issue("language", f"speech {i + 1} is marked English but has no English words")
            if needed > end - start + EPS:
                issue("speech_budget", f"speech {i + 1}: {words} words need about {needed:.2f}s at {rate:g} words/s; window {end-start:.2f}s")
            estimates.append({"line": i + 1, "words": words, "estimated_seconds": round(needed, 3)})
        elif language.lower().split("-")[0] != "en":
            estimates.append({"line": i + 1, "note": "Non-English pace needs manual review; only the time window was checked."})
        parsed.append((start, end, speaker, overlap, i + 1))

    parsed.sort()
    for i, a in enumerate(parsed):
        for b in parsed[i + 1:]:
            if b[0] >= a[1] - EPS:
                break
            if min(a[1], b[1]) <= max(a[0], b[0]) + EPS:
                continue
            if a[2] == b[2] or not (a[3] and b[3]):
                issue("speech_overlap", f"speech {a[4]} and {b[4]} overlap without an explicit two-speaker overlap")
    return {"passed": not issues, "duration": duration, "issues": issues,
            "speech_estimates": estimates,
            "scope": "Timing ledger only; manually verify prompt agreement, physical continuity, acting and generated video."}


def main():
    parser = argparse.ArgumentParser(description=__doc__, epilog='JSON: {"duration":15,"segments":[{"start":0,"end":15}],"speech":[{"speaker":"A","start":1,"end":3,"text":"Come here.","language":"en","words_per_second":2,"overlap":false}]}')
    parser.add_argument("schedule", type=Path)
    args = parser.parse_args()
    try:
        result = audit(json.loads(args.schedule.read_text(encoding="utf-8")))
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"passed": False, "input_error": str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
