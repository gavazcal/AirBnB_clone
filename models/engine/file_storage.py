#!/usr/bin/python3
"""
Create of class FileStorage that cereals and decereals JSON
"""
import json


class FileStorage:
    """
    Cereals and decereals JSON file to instances
    """
    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """ Returns the dictionary """
        return self.__objects

    def new(self, obj):
        """ Add object to dictionary objects """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """ cerealizes objects to JSON file, path: __file_path """
        filename = self.__file_path
        new_dic = {}
        with open(filename, mode='w', encoding='UTF-8') as myFile:
            for key, value in self.__objects.items():
                new_dic[key] = value
            json.dump(self.__objects, myFile)


    def reload(self):
        try:
            filename = self.__file_path
            with open(filename, mode='r', encoding='UTF-8') as myFile:
                json.load(myFile)
        except:
            pass
