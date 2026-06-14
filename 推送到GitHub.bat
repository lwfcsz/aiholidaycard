@echo off
chcp 65001 >nul
echo ================================================
echo     GitHub 部署脚本
echo ================================================
echo.

echo 请按照以下步骤操作：
echo.
echo 1. 访问 https://github.com 并登录
echo 2. 点击右上角 "+" -> "New repository"
echo 3. 仓库名称填写：ai-greeting-card
echo 4. 选择 "Private"（私有）或 "Public"（公开）
echo 5. 点击 "Create repository"
echo.
echo 6. 创建仓库后，复制仓库的URL
echo    格式应该是：https://github.com/你的用户名/ai-greeting-card.git
echo.
echo 请在下方粘贴你的仓库URL：
echo （按回车键继续，或直接关闭窗口）
echo.

set /p repo_url="仓库URL: "

if "%repo_url%"=="" (
    echo 错误：未输入仓库URL
    pause
    exit /b 1
)

echo.
echo 正在配置远程仓库...
git remote add origin %repo_url%

echo.
echo 正在推送代码到GitHub...
git branch -M main
git push -u origin main

echo.
echo ================================================
echo     部署完成！
echo ================================================
echo.
echo ✓ 代码已推送到GitHub
echo.
echo 你的仓库地址：%repo_url%
echo.
pause