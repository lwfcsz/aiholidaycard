@echo off
chcp 65001 >nul
title AI节日贺卡生成系统 - 前端服务

echo ======================================
echo   AI节日贺卡生成系统 - 前端服务启动
echo ======================================
echo.

cd /d "%~dp0frontend"

echo [1/3] 检查Node.js环境...
node --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到Node.js，请先安装Node.js 16+
    pause
    exit /b 1
)

echo [2/3] 安装前端依赖...
call npm install
if errorlevel 1 (
    echo [错误] 依赖安装失败
    pause
    exit /b 1
)

echo [3/3] 启动前端服务...
echo.
echo 访问地址：http://localhost:5173
echo.
echo 按 Ctrl+C 停止服务
echo.

npm run dev

pause
