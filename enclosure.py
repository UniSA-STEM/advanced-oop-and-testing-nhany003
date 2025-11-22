'''
File: filename.py
Description: A brief description of this Python module.
Author: Nenciliae Nhanga
ID: 110424563
Username: nhany003
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    def __init__(self, name, size, environment_type,  capacity):
        self.__name = name
        self.__size = size
        self.__environment_type = environment_type
        self.__capacity = capacity
        self.__cleanliness_level = 100
        self.__animals = []
        self.__allowed_species = None

    # Getters
    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_environment_type(self):
        return self.__environment_type

    def get_capacity(self):
        return self.__capacity

    def get_cleanliness_level(self):
        return self.__cleanliness_level

    def get_animals(self):
        return self.__animals

    def get_allowed_species(self):
        return self.__allowed_species

    # Setters
    def set_cleanliness_level(self, level):
        self.__cleanliness_level = level

    def set_allowed_species(self, species):
        self.__allowed_species = species

    def can_add_animal(self, animal):
        """Check if an animal can be added to this enclosure"""
        if len(self.__animals) >= self.__capacity:
            return False, "Enclosure is at full capacity"

        if animal.has_active_health_issues():
            return False, "Animal is under treatment and cannot be moved"

        if animal.get_preferred_environment() != self.__environment_type:
            return False, f"Environment mismatch"

        if self.__allowed_species is None:
            return True, "OK"
        elif self.__allowed_species == animal.get_species():
            return True, "OK"
        else:
            return False, f"Enclosure already houses {self.__allowed_species}"

    def add_animal(self, animal):
        """Add an animal to the enclosure"""
        can_add, message = self.can_add_animal(animal)
        if can_add:
            self.__animals.append(animal)
            animal.set_enclosure(self)
            if self.__allowed_species is None:
                self.__allowed_species = animal.get_species()
            return True
        else:
            print(f"Cannot add {animal.get_name()}: {message}")
            return False

    def remove_animal(self, animal):
        """Remove an animal from the enclosure"""
        if animal in self.__animals:
            self.__animals.remove(animal)
            animal.set_enclosure(None)
            if len(self.__animals) == 0:
                self.__allowed_species = None
            return True
        return False

    def clean(self, amount=20):
        """Clean the enclosure"""
        self.__cleanliness_level = min(100, self.__cleanliness_level + amount)

    def degrade_cleanliness(self, amount=5):
        """Reduce cleanliness level"""
        self.__cleanliness_level = max(0, self.__cleanliness_level - amount)

    def get_status(self):
        """Get the current status of the enclosure"""
        status = f"Enclosure: {self.__name}\n"
        status += f"  Environment: {self.__environment_type}\n"
        status += f"  Size: {self.__size}m²\n"
        status += f"  Capacity: {len(self.__animals)}/{self.__capacity}\n"
        status += f"  Cleanliness: {self.__cleanliness_level}%\n"
        status += f"  Animals: {len(self.__animals)}\n"
        for animal in self.__animals:
            status += f"    - {animal}\n"
        return status

    def list_animals(self):
        """List all animals in the enclosure"""
        return self.__animals

    def __str__(self):
        return f"{self.__name} ({self.__environment_type}) - {len(self.__animals)}/{self.__capacity} animals"

