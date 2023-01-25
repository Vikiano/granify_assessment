# class Cat:
#     def __init__(self):
#         self.name = None
#         self.age = None
#         self.favoriteFood = None

#     def getName(self):
#         return self.name
    
#     def getAge(self):
#         return self.age
    
#     def getFavoriteFood(self):
#         return self.favoriteFood
    
#     def setName(self, newName):
#         self.name = newName
    
#     def setAge(self, newAge):
#         self.age = newAge
    
#     def setFavoriteFood(self, newFavoriteFood):
#         self.favoriteFood = newFavoriteFood

import random

class Cat:
    def __init__(self, name=None):
        self.name = name
        self.age = random.randint(5, 10)
        self.favoriteFood = None
        self.names = []
        if self.name:
            self.names.append(self.name)

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getFavoriteFood(self):
        return self.favoriteFood
    
    def setName(self, newName):
        self.name = newName
        self.names.append(newName)
    
    def setAge(self, newAge):
        self.age = newAge
    
    def setFavoriteFood(self, newFavoriteFood):
        self.favoriteFood = newFavoriteFood
        
    def speak(self, message=None):
        
        if message is None:
            print("meow")
        if message:
            print(message)
        else:
            print("meow")
            
    def getNames(self):
        return self.names
    
    def getAverageNameLength(self):
        total_length = 0
        for name in self.names:
            total_length += len(name)
        return total_length / len(self.names)

