# One Shot · 即梦电影提示词

**作者：[gerrywrittenhousea76-design](https://github.com/gerrywrittenhousea76-design)**

**仅限非商业使用；禁止未经授权的镜像搬运、改名重发和商业使用。商用须先联系作者取得书面许可。**

[完整许可](LICENSE.md) · [申请商用授权](https://github.com/gerrywrittenhousea76-design/one-shot/issues/new?template=commercial-license.yml)

把一句故事线扩写为结构完整的中文电影提示词，覆盖人物、场景、镜头、表演、英文对白、声音和连续性。

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

本仓库公开，允许在 [LICENSE.md](LICENSE.md) 规定范围内进行个人非商业学习、测试和创作，并保留安装、更新及个人备份必需的本地副本。商业使用和未经授权的再发布不在此授权范围内。

在 Codex 中直接发送这一句即可让内置安装器安装：

```text
使用 $skill-installer，从 https://github.com/gerrywrittenhousea76-design/one-shot 安装 one-shot，技能位于仓库根目录。
```

也可使用 [Skills CLI](https://github.com/vercel-labs/skills) 在终端安装；需要 Node.js / npm：

```bash
npx skills add gerrywrittenhousea76-design/one-shot --skill one-shot --agent codex -g
```

这是给当前用户的 Codex 安装。安装后直接输入 `$one-shot` 加故事线即可调用；如果当前会话没有发现新技能，重新打开 Codex 会话。

如需手动安装，可从本仓库的 **Code → Download ZIP** 下载，将解压后的文件夹命名为 `one-shot`，放进 Codex 的 skills 目录，确保目录内直接存在 `SKILL.md`，并保留 `LICENSE.md` 与作者署名。安装器内部为安装创建的临时克隆或缓存属于许可中的安装例外，不代表可以另建镜像、改名重发或出售。

### 按名称搜索

在 Skills 社区目录中搜索：

```bash
npx skills find one-shot
```

认准来源 `gerrywrittenhousea76-design/one-shot`，避免安装同名技能。社区目录的收录和搜索更新可能有延迟；未搜到时使用上面的安装命令即可，不需要等待收录。按 [Skills 的收录说明](https://skills.sh/docs/faq)，目录通过实际安装数据发现技能；仓库公开不代表已经进入 Codex 官方内置目录。

## 内容

- [主指令](SKILL.md)：默认行为、工作流程与资源选择。
- [情绪对白示例](examples/last-train.md)、[动作长镜头示例](examples/luggage-chase.md)、[厚涂示例](examples/painter.md)、[国家与语言覆盖示例](examples/override.md)。
- [质量检查](references/quality-gate.md) 与 [验证记录](evals/validation-report.md)。
- `scripts/audit_timing.py`：可选的本地时间表检查，仅依赖 Python 3 标准库。

## 范围与质量目标

只创作提示词，不自动提交即梦任务或消耗生成额度。即梦不同入口的能力需按实际界面确认；默认 15 秒制作分段约定不代表所有版本的硬上限。

“提升约 30%”是七维对照改进目标，不能通过字数增加或自评分证明。仓库验证记录区分文本检查与实际视频测试。

## 作者署名、商用与复制限制

One Shot 的作者署名为 **gerrywrittenhousea76-design**。本项目采用自定义受限许可，并非可自由商用、改名或再分发的开放源代码许可证。使用本 Skill 制作广告、品牌内容、客户委托作品、收费服务或商业产品，须先取得作者书面许可；免费安装不等于获得商用授权。

请通过 [商用授权申请](https://github.com/gerrywrittenhousea76-design/one-shot/issues/new?template=commercial-license.yml) 联系作者，说明用途、渠道、期限及是否涉及分发。保留作者署名、提交申请或作者没有回复，均不构成授权。

**公开仓库不能从技术上禁止 Git 克隆，GitHub 也允许站内 Fork。** 本项目限制的是平台已授予权利和安装例外之外的镜像搬运、改名重发、再分发及商业使用，不声称已关闭 Fork 或下载功能。具体边界见 [LICENSE.md](LICENSE.md) 和 [GitHub 公开仓库许可说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)。

## 时间检查示例

```bash
python3 scripts/audit_timing.py evals/timing-pass.json
```

此工具检查时间覆盖、对白窗口和英语语速预算；它不验证镜头几何、成片质量，也不替代对最终提示词的审查。
