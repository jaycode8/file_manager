import os
import shutil

class FileManager:
    def __init__(self, path):
        self.path = path

        self.file_types = {
            "IMAGES": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp", ".webp", ".tiff"],
            "DOCUMENTS": [".pdf", ".docx", ".doc", ".txt", ".csv", ".xlsx", ".pptx", ".odt"],
            "PROGRAMMING": [".json", ".xml", ".html", ".css", ".js", ".ts", ".py", ".ipynb", ".cpp", ".java", ".php", ".go", ".rs"],
            "MEDIA": [".mp4", ".mkv", ".mov", ".avi", ".mp3", ".wav", ".flac"],
            "SOFTWARES": [".exe", ".msi", ".deb", ".rpm", ".dmg", ".apk"],
            "ARCHIVES": [".zip", ".rar", ".tar", ".gz", ".7z"],
            "SPREADSHEETS": [".xls", ".xlsx", ".ods"],
            "PRESENTATIONS": [".ppt", ".pptx", ".odp"],
            "DATABASES": [".sql", ".sqlite", ".db", ".mdb"],
            "CONFIGURATION": [".ini", ".cfg", ".yaml", ".yml", ".env"],
            "BACKUPS": [".bak"]
        }

    def files(self):
        return [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]

    def list_files(self):
        files = self.files()
        if files:
            print("\nFiles in the directory:")
            for file in files:
                print(f"- {file}")
        else:
            print("\n❌ No files found in the directory.")

    def directories(self):
        return [f for f in os.listdir(self.path) if os.path.isdir(os.path.join(self.path, f))]

    def list_directories(self):
        directories = self.directories()
        if directories:
            print("\Sub-Directories in the directory:")
            for directory in directories:
                print(f"- {directory}")
        else:
            print("\n❌ No sub-directories found.")

    def create_directories(self, name):
        dir_path = os.path.join(self.path, name)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

    def move_files(self):
        for file in self.files():
            _, ext = os.path.splitext(file)
            ext = ext.lower()

            for category, extensions in self.file_types.items():
                if ext in extensions:
                    self.create_directories(category)
                    shutil.move(os.path.join(self.path, file), os.path.join(self.path, category, file))
                    break

    def organize(self):
        if self.files():
            self.move_files()
            print("\n✅ Files have been organized successfully.")
        print("\n❌ No files detected in the root directory")

    def rename_files(self):
        files = self.files()
        for i,file_name in enumerate(files):
            _, ext = os.path.splitext(file_name)
            os.rename(os.path.join(self.path,file_name), os.path.join(self.path, f"file_{str(i+1).zfill(3)}{ext}"))
        print("\n✅ Successfully renamed all files.")

if __name__ == "__main__":
    path = input("Enter the directory path to your files\n>>>").strip()
    
    if not os.path.exists(path):
        print("\n❌ The specified path does not exist. Please check and try again.")
    else:
        manager = FileManager(path)

        print("\nChoose an option:")
        print("1. List files")
        print("2. List directories")
        print("3. Organize files")
        print("4. Rename files")
        choice = input("\n>>>").strip()

        if choice == "1":
            manager.list_files()
        elif choice == "2":
            manager.list_directories()
        elif choice == "3":
            manager.organize()
        elif choice == "4":
            manager.rename_files()
        else:
            print("\n❌ Invalid option. Exiting program.")
