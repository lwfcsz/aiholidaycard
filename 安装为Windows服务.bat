@echo off
chcp 65001 >nul
echo ================================================
echo     AI节日贺卡系统 - Windows服务安装脚本
echo ================================================
echo.

:: 检查管理员权限
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 请右键选择"以管理员身份运行"此脚本
    pause
    exit /b 1
)

echo [1/3] 检查nssm工具...
if not exist "nssm.exe" (
    echo 下载nssm工具...
    powershell -Command "Invoke-WebRequest -Uri 'https://nssm.cc/release/nssm-2.24.zip' -OutFile 'nssm.zip'"
    powershell -Command "Expand-Archive -Path 'nssm.zip' -DestinationPath '.' -Force"
    move /Y "nssm-2.24\win64\nssm.exe" . >nul 2>&1
    rd /S /Q "nssm-2.24" 2>nul
    del /Q "nssm.zip" 2>nul
)
echo ✓ nssm工具已就绪

echo.
echo [2/3] 安装Python依赖...
cd backend
if not exist "venv" (
    python -m venv venv
)
call venv\Scripts\activate.bat
pip install -q -r requirements.txt
cd ..

echo.
echo [3/3] 注册Windows服务...
nssm.exe install "AIGreetingCard" "python" "backend\app.py"
nssm.exe set "AIGreetingCard" "AppDirectory" "%CD%\backend"
nssm.exe set "AIGreetingCard" "DisplayName" "AI节日贺卡系统"
nssm.exe set "AIGreetingCard" "Description" "AI节日贺卡生成系统服务"
nssm.exe set "AIGreetingCard" "Start" "auto"

echo.
echo ================================================
echo     服务安装成功！
echo ================================================
echo.
echo 启动服务中...
net start AIGreetingCard

echo.
echo ✓ 服务已启动！
echo.
echo 访问地址：http://localhost:8000
echo.
echo 服务管理命令：
echo   启动服务：net start AIGreetingCard
echo   停止服务：net stop AIGreetingCard
echo   卸载服务：nssm.exe remove AIGreetingCard
echo.
pause