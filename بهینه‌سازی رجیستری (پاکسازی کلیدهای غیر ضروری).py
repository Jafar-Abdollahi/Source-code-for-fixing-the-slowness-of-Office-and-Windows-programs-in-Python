def clean_registry():
    keys_to_delete = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run32",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run"
    ]

    for key in keys_to_delete:
        try:
            reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key, 0, winreg.KEY_ALL_ACCESS)
            while True:
                try:
                    subkey = winreg.EnumValue(reg_key, 0)
                    winreg.DeleteValue(reg_key, subkey[0])
                except OSError:
                    break
            winreg.CloseKey(reg_key)
            print(f"Cleaned registry key: {key}")
        except Exception as e:
            print(f"Error cleaning registry key {key}: {e}")

clean_registry()
