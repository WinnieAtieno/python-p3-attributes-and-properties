#!/usr/bin/env python3




class Dog:
    # List of approved breeds
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
 
    def __init__(self, name = None, breed=None):
        if name is not None:
            self.set_name(name)
        else:
            self.name = None
        
        if breed is not None:
            self.set_breed(breed)
        else:
            self.breed = None

    def set_name(self, name):
        if not isinstance(name, str) or len(name) == 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            self.name = None
        else:
            self.name = name

    def set_breed(self, breed):
        if breed not in self.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            self.breed = None
        else:
            self.breed = breed

    
fido = Dog("Fido")
print(fido.name)
      
   

