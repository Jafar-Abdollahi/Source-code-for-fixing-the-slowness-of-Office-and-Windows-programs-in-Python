import winreg

def list_startup_programs():
    startup_keys = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"
    ]

    for key in startup_keys:
        try:
            reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key)
            print(f"Listing startup programs from: {key}")
            i = 0
            while True:
                try:
                    value = winreg.EnumValue(reg_key, i)
                    print(f"{value[0]}: {value[1]}")
                    i += 1
                except OSError:
                    break
            winreg.CloseKey(reg_key)
        except Exception as e:
            print(f"Error accessing registry key {key}: {e}")

list_startup_programs()
