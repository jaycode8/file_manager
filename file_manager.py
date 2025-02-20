import os

class FileManager():
    def __init__(self, path):
        self.path = path
        self.directory = ""
        self.type_image = [".jpg", ".png", ".jpeg", ".svg"]
        self.type_docs = [".pdf", ".docx"]
        self.type_code = [".json", ".ipynb", ".xml", ".json"]
        self.type_media = [".mp4"]
        self.type_software = [".deb"]

    def files(self):
        files = os.listdir(self.path)
        return files

    def rename(self):
        pass

    def create_directories(self, name):
        if os.path.exists(name):
            print(f"The directory {name} already exists")
        else:
            os.mkdir(name)

    def extensions(self):
        files = self.files()
        extensions = []
        for i, file_name in enumerate(files):
            file_name, file_extension = os.path.splitext(file_name)
            extensions.append(file_extension)
        return extensions

    def organize(self):
        extensions = self.extensions()

        if any(file_type in extensions for file_type in self.type_image):
            self.create_directories("IMAGES")

        if any(file_type in extensions for file_type in self.type_docs):
            self.create_directories("DOCUMENTS")

        if any(file_type in extensions for file_type in self.type_code):
            self.create_directories("PROGRAMMING")

        if any(file_type in extensions for file_type in self.type_media):
            self.create_directories("MEDIA")

        if any(file_type in extensions for file_type in self.type_software):
            self.create_directories("SOFTWARES")

        files = self.files()
        for file in files:
            if file.endswith(".jpg"):
                print("found image")
        # return files

if __name__ == "__main__":
    # path = input("Enter the path to your files\n>>>")
    path = "/home/jaymoh/Downloads/multiples"
    manager = FileManager(path)
    print(manager.organize())