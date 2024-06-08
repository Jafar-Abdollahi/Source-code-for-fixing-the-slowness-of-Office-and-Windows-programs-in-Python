import os
import shutil

def clear_temp_files():
    temp_dirs = [os.getenv('TEMP'), os.getenv('TMP')]
    for temp_dir in temp_dirs:
        if os.path.isdir(temp_dir):
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                    except Exception as e:
                        print(f"Error removing file {file}: {e}")
                for dir in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, dir))
                    except Exception as e:
                        print(f"Error removing directory {dir}: {e}")
    print("Temporary files cleaned.")

clear_temp_files()
