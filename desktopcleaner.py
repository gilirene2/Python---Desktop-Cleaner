import os
import shutil

def clean_desktop(desktop_path):
    # Dictionary to map file extensions to folder names
    folders = {
        "Documents": [".pdf", ".doc", ".docx", ".txt"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Music": [".mp3", ".wav"],
        "Others": []  # Default folder for other file types
    }

    # Create folders if they don't exist
    for folder in folders.keys():
        folder_path = os.path.join(desktop_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to appropriate folders
    for file in os.listdir(desktop_path):
        if file != "desktop_cleaner.py":  # Exclude the script itself
            file_path = os.path.join(desktop_path, file)
            if os.path.isfile(file_path):
                for folder, extensions in folders.items():
                    if any(file.lower().endswith(ext) for ext in extensions):
                        destination = os.path.join(desktop_path, folder, file)
                        shutil.move(file_path, destination)
                        print(f"Moved {file} to {folder} folder.")
                        break
                else:
                    destination = os.path.join(desktop_path, "Others", file)
                    shutil.move(file_path, destination)
                    print(f"Moved {file} to Others folder.")

if __name__ == "__main__":
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    clean_desktop(desktop_path)
