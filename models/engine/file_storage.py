import json


from ..base_model import BaseModel
class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
                
    def new(self, obj):
        key = obj.__class__.__name__ + obj.id
        value = obj.to_dict()
        FileStorage.__objects.update({key: value})

    def save(self):
        if FileStorage.__objects:
            with open(FileStorage.__file_path, 'a') as file:
                    json.dump(FileStorage.__objects, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                FileStorage.__objects = json.load(file)
        except (FileExistsError, FileNotFoundError, json.decoder.JSONDecodeError):
            pass
