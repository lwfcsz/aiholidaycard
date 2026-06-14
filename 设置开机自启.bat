@echo off
chcp 65001 >nul
echo ================================================
echo     AI节日贺卡系统 - 开机自启设置
echo ================================================
echo.

echo [1/2] 创建开机自启脚本...
echo @echo off > "启动AI贺卡系统.bat"
echo cd /d "%%~dp0backend" >> "启动AI贺卡系统.bat"
echo if not exist "venv" ( >> "启动AI贺卡系统.bat"
echo     python -m venv venv >> "启动AI贺卡系统.bat"
echo ) >> "启动AI贺卡系统.bat"
echo call venv\Scripts\activate.bat >> "启动AI贺卡系统.bat"
echo python app.py >> "启动AI贺卡系统.bat"
echo.

echo [2/2] 添加到开机自启...
copy "启动AI贺卡系统.bat" "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\" /Y

echo.
echo ================================================
echo     设置成功！
echo ================================================
echo.
echo ✓ 已创建启动脚本：启动AI贺卡系统.bat
echo ✓ 已添加到开机自启
echo.
echo 下次开机时服务将自动启动
echo.
pause