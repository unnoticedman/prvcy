@echo off
:: Ruta completa al ejecutable de Python
set python_exe="...\python.exe"
:: Ruta completa al script de Python
set script_path="...\prvcy.py"

:: Comprobar si el script se está ejecutando con permisos de administrador
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Ejecutando el script como administrador...
    %python_exe% %script_path%
) else (
    echo Solicitud de permisos de administrador...
    powershell -Command "Start-Process cmd -ArgumentList '/c %python_exe% %script_path%' -Verb runAs"
)
pause
