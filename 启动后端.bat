@echo off
chcp 65001 >nul
title AI节日贺卡生成系统 - 后端服务

echo ======================================
echo   AI节日贺卡生成系统 - 后端服务启动
echo ======================================
echo.

cd /d "%~dp0backend"

echo [1/3] 检查Python环境...
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到Python，请先安装Python 3.8+
    pause
    exit /b 1
)

echo [2/3] 安装依赖包...
pip install -r requirements.txt -q
if errorlevel 1 (
    echo [错误] 依赖安装失败
    pause
    exit /b 1
)

echo [3/3] 启动后端服务...
echo.
echo 服务地址：http://localhost:8000
echo API文档：http://localhost:8000/docs
echo.
echo 按 Ctrl+C 停止服务
echo.

python app.py

pause
