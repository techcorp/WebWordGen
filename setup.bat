@echo off
echo Setting up WebWordGen...
:: Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Error: Python is not installed. Please install Python 3.7+ from https://www.python.org/
    pause
    exit /b
)
:: Install dependencies
pip install -r requirements.txt
:: Create output directory
if not exist output mkdir output
echo Setup complete! Run: python webwordgen.py
pause
