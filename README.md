# One Shot · 即梦电影提示词

把一句故事线扩写为结构完整的中文电影提示词，覆盖人物、场景、镜头、表演、英文对白、声音和连续性。基于使用者提供并确认的十三份 DOCX 材料提炼。

名称意为“一句话，生成一份完整电影提示词”。镜头形式仍根据故事选择，也可按用户要求使用一镜到底。

## 使用

安装后输入：

```text
使用 $one-shot：一位退休列车司机在末班车站台遇见多年未见的女儿。
```

也可以明确覆盖默认值：

```text
使用 $one-shot：15 秒，日本父亲在学校门口接到不愿回家的女儿。全部中文对白，写实电影，多镜头。
```

默认正文中文、对白英文、人物欧美背景。Skill 根据故事决定时长和镜头形式，允许补足动机、冲突和结局，保留故事核心。用户指定的国家、语言、风格、时长等优先。没有参考图也能生成完整提示词。

输出直接是提示词文档；日常使用无需先完成访谈。较长作品按自然剪辑点给出独立可复制的生成段，严格一镜到底要求单独处理。

## 安装

本仓库公开，任何人都可以下载和安装，不需要获得本仓库的访问授权。

在 Codex 中直接发送这一句即可让内置安装器安装：

```text
使用 $skill-installer，从 https://github.com/gerrywrittenhousea76-design/one-shot 安装 one-shot，技能位于仓库根目录。
```

也可使用 [Skills CLI](https://github.com/vercel-labs/skills) 在终端安装；需要 Node.js / npm：

```bash
npx skills add gerrywrittenhousea76-design/one-shot --skill one-shot --agent codex -g
```

这是给当前用户的 Codex 安装。安装后直接输入 `$one-shot` 加故事线即可调用；如果当前会话没有发现新技能，重新打开 Codex 会话。

如需手动安装，将本仓库文件夹放进 Codex 的 skills 目录，确保目录内直接存在 `SKILL.md`。下面的命令在目标目录已存在时会停止，不覆盖原文件：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/gerrywrittenhousea76-design/one-shot.git "${CODEX_HOME:-$HOME/.codex}/skills/one-shot"
```

### 按名称搜索

在 Skills 社区目录中搜索：

```bash
npx skills find one-shot
```

认准来源 `gerrywrittenhousea76-design/one-shot`，避免安装同名技能。社区目录的收录和搜索更新可能有延迟；未搜到时使用上面的安装命令即可，不需要等待收录。按 [Skills 的收录说明](https://skills.sh/docs/faq)，目录通过实际安装数据发现技能；仓库公开不代表已经进入 Codex 官方内置目录。

## 内容

- [主指令](SKILL.md)：默认行为、工作流程与资源选择。
- [方法来源](references/source-distillation.md)：十三篇的具体贡献、适用范围和修正点。
- [情绪对白示例](examples/last-train.md)、[动作长镜头示例](examples/luggage-chase.md)、[厚涂示例](examples/painter.md)、[国家与语言覆盖示例](examples/override.md)。
- [质量检查](references/quality-gate.md) 与 [验证记录](evals/validation-report.md)。
- `scripts/audit_timing.py`：可选的本地时间表检查，仅依赖 Python 3 标准库。

## 范围与质量目标

只创作提示词，不自动提交即梦任务或消耗生成额度。即梦不同入口的能力需按实际界面确认；默认 15 秒制作分段约定不代表所有版本的硬上限。

“提升约 30%”是七维对照改进目标，不能通过字数增加或自评分证明。仓库验证记录区分文本检查与实际视频测试。原始 DOCX、视频、登录凭证和个人文件路径不随 Skill 分发。

## 时间检查示例

```bash
python3 scripts/audit_timing.py evals/timing-pass.json
```

此工具检查时间覆盖、对白窗口和英语语速预算；它不验证镜头几何、成片质量，也不替代对最终提示词的审查。
