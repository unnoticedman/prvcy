import os
import random
import subprocess
import json

# Nombre de la interfaz Wi-Fi
WIFI_INTERFACE = "Wi-Fi"

# Archivo donde se guardará la MAC original
MAC_FILE = "wifi_original_mac.json"

def get_random_mac():
    """Genera una dirección MAC aleatoria."""
    return "02:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def change_mac(interface, new_mac):
    """Cambia la dirección MAC de una interfaz específica en Windows."""
    try:
        print(f"Cambiando la MAC de {interface} a {new_mac}")
        # Deshabilitar la interfaz de red
        os.system(f"netsh interface set interface \"{interface}\" admin=disable")
        
        # Cambiar la dirección MAC en el registro de Windows
        subprocess.call(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4d36e972-e325-11ce-bfc1-08002be10318}}\\0001" /v NetworkAddress /d {new_mac.replace(":", "")} /f', shell=True)
        
        # Habilitar la interfaz de red nuevamente
        os.system(f"netsh interface set interface \"{interface}\" admin=enable")
        
        print(f"MAC de {interface} cambiada a {new_mac}")
    except Exception as e:
        print(f"Error al cambiar la dirección MAC: {e}")

def save_original_mac(interface):
    """Guarda la MAC original de la interfaz."""
    output = subprocess.check_output(f"getmac /v /fo list | findstr /C:{interface}", shell=True, encoding='cp1252')
    mac_address = output.splitlines()[0].split()[1]
    return mac_address

def change_wifi_mac():
    """Cambia la MAC del Wi-Fi y guarda la original."""
    original_mac = save_original_mac(WIFI_INTERFACE)
    new_mac = get_random_mac()
    change_mac(WIFI_INTERFACE, new_mac)

    # Guardar la MAC original en un archivo
    with open(MAC_FILE, "w") as f:
        json.dump({WIFI_INTERFACE: original_mac}, f)

# Ejecución del script
if __name__ == "__main__":
    change_wifi_mac()
