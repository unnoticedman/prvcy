# Cambiar y Restaurar la Dirección MAC del Adaptador Wi-Fi

Este proyecto proporciona dos scripts de Python diseñados para cambiar y luego restaurar la dirección MAC de un adaptador Wi-Fi en un sistema Windows.

## Contenido

- [Requisitos](#requisitos)
- [Identificación del Adaptador Wi-Fi (`000x`)](#identificación-del-adaptador-wi-fi-000x)
- [Modificación de Archivos `.bat`](#modificación-de-archivos-bat)
- [Ejecución del Script para Cambiar la MAC](#ejecución-del-script-para-cambiar-la-mac)
- [Ejecución del Script para Restaurar la MAC](#ejecución-del-script-para-restaurar-la-mac)

## Requisitos

- **Sistema Operativo**: Windows 10 o posterior.
- **Python**: Python 3.6 o superior instalado.
- **Permisos de Administrador**: Los scripts deben ejecutarse con privilegios de administrador.

## Identificación del Adaptador Wi-Fi (`000x`)

Antes de poder cambiar la dirección MAC de tu adaptador Wi-Fi, necesitas identificar el número de subcarpeta (`000x`) correspondiente en el registro de Windows.

### Pasos para Encontrar el Identificador (`000x`)

1. **Abrir el Editor del Registro**:
   - Presiona `Windows + R`, escribe `regedit`, y presiona `Enter` para abrir el Editor del Registro.

2. **Navegar a la Clave de Registro**:
   - En el Editor del Registro, navega a la siguiente ruta:
     ```
     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}
     ```

3. **Buscar el Adaptador Wi-Fi**:
   - Dentro de la carpeta `{4d36e972-e325-11ce-bfc1-08002be10318}`, verás varias subcarpetas numeradas como `0000`, `0001`, `0002`, etc.
   - Haz clic en cada una de ellas hasta que encuentres una que tenga la entrada `DriverDesc` con el nombre de tu adaptador Wi-Fi, puedes también ingresar en CMD, escribir `ipconfig /all`, revisar el nombre de tu hardware Wifi y luego buscar ese nombre dentro de los registros. Lo importante es identificar la carpeta en la cual se encuentra ese registro.

4. **Anotar el Identificador**:
   - Anota el número de la carpeta (por ejemplo, `0001`). Este número es el identificador que debes usar en el script para cambiar la MAC del adaptador Wi-Fi.

## Modificación de Archivos `.bat`

Para facilitar la ejecución de los scripts con permisos de administrador, puedes usar los archivos `.bat`. En mi caso me acomoda abrir los `.py` con Visual Studio, por lo tanto tuve que crear ficheros para ejecutar de forma indirecta estos scripts.

### 1. Modifica los `.bat` con las rutas de tus ficheros

1. **Abrir un Editor de Texto**:
   - Puedes usar un editor de texto simple como el Bloc de Notas.

2. **Modifica las rutas del  `.bat`**:
   - Introduce el siguiente código en el archivo:
     ```batch
     @echo off
     :: Ruta completa al ejecutable de Python
     set python_exe="C:\ruta\a\python.exe"
     :: Ruta completa al script de cambio de MAC
     set script_path="C:\ruta\a\tu\script\prvcy.py"

     :: Ejecutar el script como administrador
     net session >nul 2>&1
     if %errorLevel% == 0 (
         echo Ejecutando el script para cambiar la MAC como administrador...
         %python_exe% %script_path%
     ) else (
         echo Solicitud de permisos de administrador...
         powershell -Command "Start-Process cmd -ArgumentList '/c %python_exe% %script_path%' -Verb runAs"
     )
     pause
     ```

3. **Guardar el Archivo `.bat`**:


## Ejecución del Script para Cambiar la MAC

1. **Ejecutar el Script de Cambio de MAC**:
   - Haz doble clic en el archivo `prvcy.bat` para ejecutar el script y cambiar la dirección MAC de tu adaptador Wi-Fi.

2. **Verificar el Cambio**:
   - Utiliza `ipconfig /all` en la terminal de Windows para verificar que la dirección MAC haya sido cambiada correctamente.

## Ejecución del Script para Restaurar la MAC

1. **Ejecutar el Script de Restauración de MAC**:
   - Después de haber terminado tu navegación o actividades, haz doble clic en el archivo `noprvcy.bat` para restaurar la dirección MAC original de tu adaptador Wi-Fi.

2. **Verificar la Restauración**:
   - Utiliza `ipconfig /all` para verificar que la dirección MAC original haya sido restaurada.

## Notas Finales

- **Permisos de Administrador**: Ambos archivos `.bat` requieren permisos de administrador para funcionar correctamente. Esto es necesario para que el script pueda realizar cambios en el registro de Windows y modificar la dirección MAC del adaptador Wi-Fi.

- **Verificación Manual**: Es recomendable verificar manualmente que los cambios se han aplicado correctamente, tanto el cambio de la MAC como su restauración.

- **Disfruta un poco más de privacidad**: Cambiar la MAC permite obtener una pequeña capa de privacidad, ya que escondes el identificador de tu hardware de red, esto te permitirá navegar un poco más seguro y "anónimo". Es un script muy simple, pero eficaz. Combínalo con una VPN, Máquina virtual o lo que consideres necesario para poder navegar de forma privada y segura. 