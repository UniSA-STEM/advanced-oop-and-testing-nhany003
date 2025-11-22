'''
File: filename.py
Description: A brief description of this Python module.
Author: Nenciliae Nhanga
ID: 110424563
Username: nhany003
This is my own work as defined by the University's Academic Integrity Policy.
'''


class Staff:
    def __init__(self, name, employee_id):
        self.__name = name
        self.__employee_id = employee_id
        self.__assigned_animals = []
        self.__assigned_enclosures = []

    # Getters
    def get_name(self):
        return self.__name

    def get_employee_id(self):
        return self.__employee_id

    def get_assigned_animals(self):
        return self.__assigned_animals

    def get_assigned_enclosures(self):
        return self.__assigned_enclosures

    def assign_animal(self, animal):
        """Assign an animal to this staff member"""
        if animal not in self.__assigned_animals:
            self.__assigned_animals.append(animal)

    def assign_enclosure(self, enclosure):
        """Assign an enclosure to this staff member"""
        if enclosure not in self.__assigned_enclosures:
            self.__assigned_enclosures.append(enclosure)

    def get_role(self):
        """Get the role of this staff member"""
        return "Staff"

    def __str__(self):
        return f"{self.__name} ({self.get_role()}) - ID: {self.__employee_id}"


class Zookeeper(Staff):
    def get_role(self):
        return "Zookeeper"

    def feed_animal(self, animal):
        """Feed an assigned animal"""
        if animal in self.get_assigned_animals() or animal.get_enclosure() in self.get_assigned_enclosures():
            return f"{self.get_name()} fed {animal.get_name()}: {animal.eat()}"
        return f"{self.get_name()} is not assigned to {animal.get_name()}"

    def clean_enclosure(self, enclosure):
        """Clean an assigned enclosure"""
        if enclosure in self.get_assigned_enclosures():
            enclosure.clean()
            return f"{self.get_name()} cleaned {enclosure.get_name()}. Cleanliness now at {enclosure.get_cleanliness_level()}%"
        return f"{self.get_name()} is not assigned to {enclosure.get_name()}"


class Veterinarian(Staff):
    def get_role(self):
        return "Veterinarian"

    def conduct_health_check(self, animal):
        """Conduct a health check on an assigned animal"""
        if animal in self.get_assigned_animals():
            health_status = "has active health issues" if animal.has_active_health_issues() else "is healthy"
            return f"{self.get_name()} examined {animal.get_name()}. {animal.get_name()} {health_status}."
        return f"{self.get_name()} is not assigned to {animal.get_name()}"

    def treat_animal(self, animal, record):
        """Treat an animal for a health issue"""
        if animal in self.get_assigned_animals():
            if record in animal.get_health_records():
                record.mark_resolved()
                return f"{self.get_name()} treated {animal.get_name()} for: {record.get_description()}"
        return f"{self.get_name()} cannot treat {animal.get_name()}"

