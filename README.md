# 即梦电影提示词

把一句故事线扩写为结构完整的中文电影提示词，覆盖人物、场景、镜头、表演、英文对白、声音和连续性。基于使用者提供并确认的十三份 DOCX 材料提炼。

## 使用

安装后输入：

```text
使用 $jimeng-cinematic-prompt：一位退休列车司机在末班车站台遇见多年未见的女儿。
```

也可以明确覆盖默认值：

```text
使用 $jimeng-cinematic-prompt：15 秒，日本父亲在学校门口接到不愿回家的女儿。全部中文对白，写实电影，多镜头。
```

默认正文中文、对白英文、人物欧美背景。Skill 根据故事决定时长和镜头形式，允许补足动机、冲突和结局，保留故事核心。用户指定的国家、语言、风格、时长等优先。没有参考图也能生成完整提示词。

输出直接是提示词文档；日常使用无需先完成访谈。较长作品按自然剪辑点给出独立可复制的生成段，严格一镜到底要求单独处理。

## 安装

将本仓库文件夹放进 Codex 的 skills 目录，确保目录内直接存在 `SKILL.md`。也可在终端执行以下命令；目标目录已存在时 `git clone` 会停止，不覆盖原文件：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/gerrywrittenhousea76-design/jimeng-cinematic-prompt.git "${CODEX_HOME:-$HOME/.codex}/skills/jimeng-cinematic-prompt"
```

私有仓库需要先登录有权访问的 GitHub 账户。新建会话后可通过技能名调用。

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
