# GitHub部署说明

## 📦 本地代码已准备就绪

代码已经在本地Git仓库中，包含以下文件：

```
├── .gitignore           # Git忽略配置
├── README.md            # 项目说明文档
├── Dockerfile           # Docker构建配置
├── docker-compose.yml   # Docker Compose配置
├── requirements.txt     # 项目依赖
├── backend/             # 后端服务
│   ├── app.py           # FastAPI主程序
│   └── requirements.txt # Python依赖
├── frontend/            # 前端页面
│   └── index.html       # Vue3前端页面
├── 一键启动.bat         # Windows一键启动
├── 设置开机自启.bat     # 开机自启设置
├── 安装为Windows服务.bat # Windows服务安装
├── 生成PPT.py           # PPT生成脚本
└── PPT项目讲解.pptx     # 项目PPT讲解
```

---

## 🚀 推送代码到GitHub

### 方式一：使用脚本（推荐）

```bash
# 双击运行
推送到GitHub.bat

# 然后输入仓库URL：
https://github.com/lwfcsz/aiholidaycard.git
```

### 方式二：手动推送

```bash
# 打开终端，进入项目目录
cd e:\保存\pythonweb全栈期末作业

# 设置远程仓库
git remote add origin https://github.com/lwfcsz/aiholidaycard.git

# 推送代码
git branch -M main
git push -u origin main
```

---

## 🔑 GitHub认证问题

如果遇到认证失败，请尝试以下方法：

### 方法1：使用GitHub Token

1. 访问 https://github.com/settings/tokens
2. 创建新Token（选择 repo 权限）
3. 推送时使用Token作为密码：

```bash
git push -u origin main
# 用户名：你的GitHub用户名
# 密码：你的Token
```

### 方法2：使用SSH（推荐）

```bash
# 生成SSH密钥（如果没有）
ssh-keygen -t ed25519 -C "your_email@example.com"

# 添加到SSH agent
ssh-add ~/.ssh/id_ed25519

# 添加公钥到GitHub
# 复制 ~/.ssh/id_ed25519.pub 内容到 GitHub -> Settings -> SSH and GPG keys

# 更新远程仓库地址
git remote set-url origin git@github.com:lwfcsz/aiholidaycard.git

# 推送
git push -u origin main
```

---

## 📋 仓库信息

| 项目 | 信息 |
|------|------|
| **用户名** | lwfcsz |
| **仓库名** | aiholidaycard |
| **仓库URL** | https://github.com/lwfcsz/aiholidaycard |
| **分支** | main |

---

## 🌐 访问仓库

创建完成后可以访问：
- GitHub仓库：https://github.com/lwfcsz/aiholidaycard
- GitHub Pages（如需部署）：https://lwfcsz.github.io/aiholidaycard

---

## 📝 后续操作

1. ✅ 确保GitHub仓库已创建
2. ✅ 代码已在本地准备就绪
3. ⬜ 推送代码到GitHub（需要网络连接）
4. ⬜ 配置GitHub Pages（如需）

---

**提示**：如果网络问题持续，可以尝试更换网络环境后重新运行推送脚本。