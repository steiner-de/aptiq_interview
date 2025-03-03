@echo off
setlocal

:: Define the name of the virtual environment
set VENV_NAME=myenv

:: Create the virtual environment
python -m venv %VENV_NAME%
if errorlevel 1 (
    echo Failed to create virtual environment.
    exit /b 1
)

echo Virtual environment '%VENV_NAME%' created successfully.

:: Activate the virtual environment
call %VENV_NAME%\Scripts\activate
if errorlevel 1 (
    echo Failed to activate virtual environment.
    exit /b 1
)

echo Virtual environment activated.

:: Install libraries from requirements.txt
if exist requirements.txt (
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Failed to install requirements.
        exit /b 1
    )
) else (
    echo requirements.txt not found.
    exit /b 1
)

echo Requirements installed successfully.

:: Execute the Python file
set PYTHON_SCRIPT=src\main.py

if exist "%PYTHON_SCRIPT%" (
    python3 "%PYTHON_SCRIPT%"
    if errorlevel 1 (
        echo Failed to execute %PYTHON_SCRIPT%.
        exit /b 1
    )
) else (
    echo %PYTHON_SCRIPT% not found.
    exit /b 1
)

echo Script executed successfully.
endlocal