'''
File: filename.py
Description: A brief description of this Python module.
Author: Nenciliae Nhanga
ID: 110100110
Username: nhany003
This is my own work as defined by the University's Academic Integrity Policy.
'''


from datetime import datetime
from typing import List, Dict, Optional

class Animal:

    def __init__(self, name, species, age, dietary_needs):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = dietary_needs
        self.__health_records = []
        self.__enclosure = None

#getters
    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def get_dietary_needs(self):
        return self.__dietary_needs

    def get_health_records(self):
        return self.__health_records

    def get_enclosure(self):
        return self.__enclosure

#setters
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_dietary_needs(self, dietary_needs):
        self.__dietary_needs = dietary_needs

    def set_enclosure(self, enclosure):
        self.__enclosure = enclosure

    #core methods
    def make_sound(self):
        return "Generic animal sound"

    def eat(self):
        return f"{self.__name} is eating {self.__dietary_needs}"

    def sleep(self):
        return f"{self.__name} is sleeping"

#Mammal subclass
class Mammal(Animal):
    def __init__(self, name, species, age, dietary_needs, environment):
        super().__init__(name, species, age, dietary_needs)
        self.__environment = environment

    def get_environment(self):
        return self.__environment

    def set_environment(self, environment):
        self.__environment = environment

    def get_category(self):
        return "Mammal"

    def get_preferred_environment(self):
        return self.__environment

    def make_sound(self):
        return f"{self.get_name()} makes a mammalian sound"


# Reptile subclass
class Reptile(Animal):
    def __init__(self, name, species, age, dietary_needs, environment):
        super().__init__(name, species, age, dietary_needs)
        self.__environment = environment

    def get_environment(self):
        return self.__environment

    def set_environment(self, environment):
        self.__environment = environment

    def get_category(self):
        return "Reptile"

    def get_preferred_environment(self):
        return self.__environment

    def make_sound(self):
        return f"{self.get_name()} hisses"


# Bird subclass
class Bird(Animal):
    def __init__(self, name, species, age, dietary_needs, environment):
        super().__init__(name, species, age, dietary_needs)
        self.__environment = environment

    def get_environment(self):
        return self.__environment

    def set_environment(self, environment):
        self.__environment = environment

    def get_category(self):
        return "Bird"

    def get_preferred_environment(self):
        return self.__environment

    def make_sound(self):
        return f"{self.get_name()} chirps and sings"