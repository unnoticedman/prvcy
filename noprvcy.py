import os
import subprocess

# Nombre de la interfaz Wi-Fi
WIFI_INTERFACE = "Wi-Fi"

# Identificador del adaptador Wi-Fi en el registro
ADAPTER_IDENTIFIER = "0001" # Debes ingresar el identificador según corresponda en cada caso

def restore_mac_to_original(interface, adapter_identifier):
    """Elimina la configuración de la MAC personalizada para restaurar la MAC original del hardware."""
    try:
        print(f"Restaurando la MAC original en {interface}...")

        # Desactivar la interfaz de red
        os.system(f"netsh interface set interface \"{interface}\" admin=disable")

        # Eliminar la clave del registro para "NetworkAddress"
        reg_key_path = f'HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4d36e972-e325-11ce-bfc1-08002be10318}}\\{adapter_identifier}'
        subprocess.call(f'reg delete "{reg_key_path}" /v NetworkAddress /f', shell=True)

        # Confirmar que la entrada fue eliminada
        print("Clave 'NetworkAddress' eliminada del registro (si existía).")

        # Habilitar la interfaz de red nuevamente para aplicar el cambio
        os.system(f"netsh interface set interface \"{interface}\" admin=enable")
        
        print(f"MAC de {interface} restaurada a la original del hardware.")
    except Exception as e:
        print(f"Error al restaurar la dirección MAC: {e}")

# Ejecución del script
if __name__ == "__main__":
    restore_mac_to_original(WIFI_INTERFACE, ADAPTER_IDENTIFIER)
