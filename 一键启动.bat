@echo off
chcp 65001 >nul
echo ==============================================
echo      AI节日贺卡生成系统 - 一键启动脚本
echo ==============================================
echo.

echo [1/4] 检查Python环境...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误：未找到Python环境，请先安装Python 3.8+
    pause
    exit /b 1
)
echo ✓ Python环境已就绪

echo.
echo [2/4] 检查并安装依赖...
cd backend
if not exist "venv" (
    echo 创建虚拟环境...
    python -m venv venv
)
call venv\Scripts\activate.bat
pip install -q -r requirements.txt
echo ✓ 依赖安装完成

echo.
echo [3/4] 启动后端服务...
echo 服务将在 http://localhost:8000 运行
start /B python app.py

echo.
echo [4/4] 等待服务启动...
timeout /t 3 /nobreak >nul

echo.
echo ==============================================
echo      服务启动成功！
echo ==============================================
echo.
echo 访问地址：http://localhost:8000
echo 分享链接格式：http://localhost:8000/card/xxx
echo.
echo 按任意键打开浏览器...
pause >nul
start http://localhost:8000