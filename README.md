# AI节日贺卡生成系统

基于Python Web全栈开发的AI节日贺卡生成系统，融合人工智能技术，支持智能祝福语生成和精美贺卡模板。

## 项目简介

这是一个智能贺卡生成平台，用户可以选择不同的节日场景和祝福风格，系统会自动生成AI祝福语，并生成精美的电子贺卡，支持一键分享。

## 功能特点

- 🎂 **生日祝福** - 温馨、幽默、优雅多种风格
- 🏮 **节日祝福** - 新春、圣诞、万圣节等
- 🎓 **毕业祝福** - 前程似锦，青春不散场
- 🌸 **通用祝福** - 日常问候，真情表达
- 🎨 **贺卡模板** - 4种精美视觉风格
- 🔗 **一键分享** - 生成唯一链接方便分享

## 技术栈

- **后端**：Python 3.9 + FastAPI
- **前端**：Vue 3 + Tailwind CSS
- **数据库**：内存存储（可扩展）
- **部署**：Docker / Windows服务

## 快速开始

### 环境要求

- Python 3.8+
- Windows / Linux / macOS

### 安装步骤

```bash
# 1. 克隆项目
git clone <repository-url>
cd pythonweb全栈期末作业

# 2. 安装依赖
cd backend
pip install -r requirements.txt

# 3. 启动服务
python app.py
```

### Docker部署

```bash
docker-compose up -d
```

### 一键启动（Windows）

双击运行 `一键启动.bat`

## 访问地址

- 本地访问：http://localhost:8000
- 分享链接：http://localhost:8000/card/{card_id}

## API接口

### 生成贺卡
```
POST /api/generate
{
  "occasion": "birthday",
  "style": "warm",
  "recipient": "朋友",
  "custom_words": "自定义祝福"
}
```

### 查看贺卡
```
GET /card/{card_id}
```

## 项目结构

```
pythonweb全栈期末作业/
├── backend/              # 后端服务
│   ├── app.py           # FastAPI主程序
│   └── requirements.txt # Python依赖
├── frontend/            # 前端页面
│   └── index.html       # Vue3前端页面
├── Dockerfile          # Docker构建配置
├── docker-compose.yml  # Docker Compose配置
├── .gitignore         # Git忽略配置
├── README.md          # 项目说明文档
├── 一键启动.bat       # Windows一键启动
├── 设置开机自启.bat   # 开机自启设置
├── 安装为Windows服务.bat # Windows服务安装
├── PPT项目讲解.pptx   # 项目PPT讲解
└── requirements.txt    # 项目依赖
```

## 部署说明

### 本地部署

1. Windows一键启动：双击 `一键启动.bat`
2. 手动启动：`cd backend && python app.py`

### 开机自启

1. 双击 `设置开机自启.bat`
2. 下次开机时服务自动启动

### Windows服务（永久运行）

1. 右键 `安装为Windows服务.bat`，选择"以管理员身份运行"
2. 服务将以后台方式永久运行

### Docker部署

```bash
docker-compose up -d
```

## 使用流程

1. 访问 http://localhost:8000
2. 选择节日场景（生日/节日/毕业/祝福）
3. 选择祝福风格（温馨/幽默/优雅）
4. 可选：填写收件人和自定义祝福语
5. 点击"生成贺卡"
6. 复制分享链接

## 开发说明

### 后端开发

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### 前端开发

前端使用Vue 3 + Tailwind CSS，直接修改 `frontend/index.html` 文件即可。

## 扩展功能

- [ ] 接入真实AI大模型（如文心一言、通义千问）
- [ ] 添加更多贺卡模板和背景
- [ ] 支持图片上传和自定义背景
- [ ] 添加用户系统和历史记录
- [ ] 贺卡导出为图片
- [ ] 添加数据库持久化存储

## 许可证

MIT License

## 作者

Python Web 全栈开发期末项目

## 版本

v1.0.0