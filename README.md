# git-ai

A tool for AI-powered git operations.

随便写的一句话，用于测试提交。

## Usage

```bash
git ai commit -m "message"
git ai diff
git ai log
```

## Git AI 归属追踪测试报告

### 环境

- OS: Windows 10.0.26200
- git-ai: v1.6.4
- OpenCode: 已安装 git-ai 插件 (`~/.config/opencode/plugins/git-ai.ts`)
- Daemon: trace2 pipe 模式运行中

### 测试结果

| 测试场景 | 提交 | 归属结果 |
|---|---|---|
| 纯 AI 修改（OpenCode） | `e84d01c` | ✅ 100% AI |
| AI + Human 混合修改 | `15f43b0` | ✅ 75% AI / 25% Human |
| 纯 Human 手动修改 | `25b29e7` | ❌ untracked |
| Human + `git ai checkpoint human` | `3f5faa5` | ❌ untracked |
| VS Code 扩展编辑（KnownHuman） | `1b115b2` | ❌ untracked（checkpoint 正确写入但 commit 时行归属丢失） |

### 已知问题

git-ai 在 Windows 上存在以下已知问题：

1. **Daemon 硬编码 PowerShell**（[#1366](https://github.com/git-ai-project/git-ai/issues/1366)）— daemon 后台进程通过 PowerShell 启动，在企业环境或 PowerShell 受限时失效。修复（[#1587](https://github.com/git-ai-project/git-ai/pull/1587)）曾合入但因引发控制台弹窗问题（[#1657](https://github.com/git-ai-project/git-ai/issues/1657)）被回滚。
2. **Checkpoint 管道通信超时** — Windows 上 `git-ai.exe checkpoint` 通过 named pipe 与 daemon 通信效率低，debug 自检中 checkpoint 命令频繁超时（0.9s-1.6s）。OpenCode 插件使用 10s 超时因此 AI 归属正常，但 `checkpoint human` 走不同路径导致 human 归属失败。
3. **归属自检失败** — `git ai debug` 中 attribution self-check 始终失败，daemon 响应超时。
4. **KnownHuman checkpoint 行归属在 commit 时丢失**（[#1388](https://github.com/git-ai-project/git-ai/issues/1388)）— VS Code 扩展的 `known_human` checkpoint 正确写入 `checkpoints.jsonl`，但 commit 处理时走了旧版 human(untracked) 的代码路径，导致 `line_attributions` 被丢弃，最终 authorship note 中只有 `humans` 声明但没有行范围映射，全部回退为 untracked。相关 issue 还有 [#1444](https://github.com/git-ai-project/git-ai/issues/1444)。

### 验证方式

```bash
# 查看 daemon 状态
git ai daemon status

# 查看未提交的 checkpoint
git ai status

# 查看提交归属记录
git ai log --oneline
git ai log --raw <commit>
```

## Notes

This file is modified by AI for testing purposes.

## License

MIT
