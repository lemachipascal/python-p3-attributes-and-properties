#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Fido", breed="Mastiff"):
        self._name = None
        self._breed = None
        
        
        
        self.name = name
        self.breed = breed

        

    def _validate_breed(self, breed):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")

    def _validate_name(self, name):
        if type(name) == str and 1 <= len(name) <= 25:
            return name
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        validated_name = self._validate_name(name)
        if validated_name is not None:
            self._name = validated_name


    @property
    def breed(self):
        return self._breed
    
    @breed.setter    
    def breed(self, breed):
        validated_breed = self._validate_breed(breed)
        if validated_breed is not None:
            self._breed = validated_breed


    


# class Human:
#     species = "Homo sapiens"
#     def __init__(self, age):
#         self.age = age

#     def get_age(self):
#         print("Retrieving age.")
#         return self._age
    
#     def set_age(self, age):
#         if (type(age) in (int, float)) and (0 <= age <= 120):
#             print (f"setting age to {age}")
#             self._age = age
#         else:
#             print("Age must be a number between 0 and 120.")

#     age = property(get_age, set_age)

# guido = Human(age=30)
# guido.age = 26
# guido.age = False
# guido.age = 56
# guido.age