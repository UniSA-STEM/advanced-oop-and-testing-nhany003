from typing import List
from animal import Animal


class Enclosure:

    def __init__(self, name, size, environment_type, capacity):
        self.__name = name
        self.__size = size
        self.__environment_type = environment_type
        self.__capacity = capacity
        self.__cleanliness_level = 100
        self.__animals: List[Animal] = []
        self.__allowed_species = None

    # --------------------
    # Getters
    # --------------------
    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    @property
    def environment_type(self):
        return self.__environment_type

    @property
    def capacity(self):
        return self.__capacity

    @property
    def cleanliness_level(self):
        return self.__cleanliness_level

    @property
    def animals(self):
        return self.__animals

    @property
    def allowed_species(self):
        return self.__allowed_species

    # --------------------
    # Setters
    # --------------------
    @cleanliness_level.setter
    def cleanliness_level(self, level):
        if level < 0 or level > 100:
            raise ValueError("Cleanliness level must be between 0 and 100")
        self.__cleanliness_level = int(level)

    @allowed_species.setter
    def allowed_species(self, species):
        self.__allowed_species = species

    # --------------------
    # Properties
    # --------------------
    @property
    def is_empty(self):
        """ checking that the enclosure is empty"""
        return len(self.__animals) == 0

    @property
    def is_at_capacity(self):
        """ checking if the enclosure is full"""
        return len(self.__animals) >= self.__capacity

    @property
    def available_space(self):
        """ checking how much space is available"""
        return self.__capacity - len(self.__animals)

    @property
    def needs_cleaning(self):
        """ check if enclosure needs cleaning"""
        return self.__cleanliness_level < 60

    # --------------------
    # Enclosure suitability
    # --------------------
    def is_suitable_for(self, species: str) -> bool:
        if self.__allowed_species is None or self.__allowed_species == species:
            return True
        return False

    # --------------------
    # Adding animals
    # --------------------
    def can_add_animal(self, animal):
        if len(self.__animals) >= self.__capacity:
            return False, "Enclosure is at full capacity"

        if animal.environment_type != self.__environment_type:
            return False, "Environment mismatch"

        if self.__allowed_species is None:
            return True, "OK"

        if animal.species != self.__allowed_species:
            return False, f"Enclosure already houses {self.__allowed_species}"

        return True, "OK"

    def add_animal(self, animal):
        can_add, message = self.can_add_animal(animal)

        if not can_add:
            print(f"Cannot add {animal.name}: {message}")
            return False

        self.__animals.append(animal)
        animal.set_enclosure(self)

        if self.__allowed_species is None:
            self.__allowed_species = animal.species

        return True

    # --------------------
    # Removing animals
    # --------------------
    def remove_animal(self, animal):
        if animal in self.__animals:
            self.__animals.remove(animal)
            animal.set_enclosure(None)

            # Reset allowed species if now empty
            if len(self.__animals) == 0:
                self.__allowed_species = None

            return True
        return False

    # --------------------
    # Cleanliness
    # --------------------
    def clean(self, amount=20):
        self.__cleanliness_level = min(100, self.__cleanliness_level + amount)

    def degrade_cleanliness(self, amount=5):
        """reducing the cleanliness"""
        self.__cleanliness_level = max(0, self.__cleanliness_level - amount)

    # --------------------
    # Info
    # --------------------
    def get_status(self):
        """ get current status of the enclosure"""
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
        """list all animals in the enclosure"""
        return self.__animals

    def __str__(self):
        return f"{self.__name} ({self.__environment_type}) - {len(self.__animals)}/{self.__capacity} animals"
