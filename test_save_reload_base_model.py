#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

new_instance = BaseModel(**obj)
print(new_instance.id ==  obj['id'])
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
new_dict = my_model.to_dict()
new_model = BaseModel(**new_dict)
print(my_model.id == new_model.id)
