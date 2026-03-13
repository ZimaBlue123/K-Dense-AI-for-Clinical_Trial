---
name: github-proxy-push
description: Diagnose Git proxy connectivity issues and push to GitHub reliably. Use when git push/pull fails to connect, errors mention 127.0.0.1 proxy, port 443, TLS/proxy failures, or when the user asks to “检查代理/推送到 GitHub”.
---

# GitHub Proxy Check & Push

## 目标

- 快速定位 Git 到 GitHub 失败是否由 **代理配置** 引起
- 在不破坏用户全局环境的前提下，用**一次性绕过代理**的方法完成 `git push`
- 必要时再做“永久修复”（仅在用户明确同意时）

## 诊断步骤（按顺序执行）

### 1) 确认远端与分支状态

```bash
git remote -v
git status
git log -5 --oneline
```

### 2) 检查 Git 配置中的 proxy（含来源）

优先用这条，一眼看到是全局还是仓库级配置：

```bash
git config --show-origin --list | rg -i "proxy"
```

重点关注是否存在类似：

- `http.proxy=http://127.0.0.1:10808`
- `https.proxy=http://127.0.0.1:10808`

### 3) 检查环境变量代理（Windows 常见）

PowerShell：

```powershell
$env:HTTP_PROXY
$env:HTTPS_PROXY
$env:ALL_PROXY
```

## 推荐推送方式：一次性绕过代理（不改全局配置）

当报错像这样时（示例）：

- `Failed to connect to github.com port 443 via 127.0.0.1`
- `Could not connect to server`

用一次性绕过代理推送：

```bash
git -c http.proxy= -c https.proxy= push origin HEAD
```

若需要推送指定分支：

```bash
git -c http.proxy= -c https.proxy= push origin main
```

## 可选：永久修复（仅在用户明确要求时）

### 方案A：删除全局 Git 代理

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

然后验证：

```bash
git config --global --list | rg -i "proxy"
```

### 方案B：改为正确的代理地址

仅当用户明确提供代理地址/端口时才执行：

```bash
git config --global http.proxy  "http://HOST:PORT"
git config --global https.proxy "http://HOST:PORT"
```

## 常见情况与处理

- **仓库提示 moved/redirected**
  - 推送可能仍成功，但建议把 `origin` 更新到新地址（用户同意后执行）：

```bash
git remote set-url origin https://github.com/<owner>/<repo>.git
git remote -v
```

- **仍然连不上 GitHub（非代理问题）**
  - 可能是网络策略/防火墙/DNS。优先让用户在同机环境验证能否访问 `github.com`，或改用公司允许的网络出口/代理。

## 交付标准（完成定义）

- `git push` 成功
- `git status` 显示本地与远端同步（不再 “ahead”）
- 如使用一次性绕过代理，不应修改用户的全局 Git 配置

