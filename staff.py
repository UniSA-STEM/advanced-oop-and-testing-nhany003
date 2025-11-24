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

    # -----------------------------
    # Getters
    # -----------------------------
    @property
    def name(self):
        return self.__name

    @property
    def employee_id(self):
        return self.__employee_id

    @property
    def assigned_animals(self):
        return self.__assigned_animals

    @property
    def assigned_enclosures(self):
        return self.__assigned_enclosures

    # -----------------------------
    # Assignment Methods
    # -----------------------------
    def assign_animal(self, animal):
        """assign an animal to this staff member"""
        if animal not in self.__assigned_animals:
            self.__assigned_animals.append(animal)

    def assign_enclosure(self, enclosure):
        """assign an enclosure to this staff member"""
        if enclosure not in self.__assigned_enclosures:
            self.__assigned_enclosures.append(enclosure)

    def get_role(self):
        """Get the role of this staff member"""
        return "Staff"

    def __str__(self):
        return (
            f"{self.__name} ({self.get_role()}) - ID: {self.__employee_id}/n"
            f"Assigned Animals: {len(self.__assigned_animals)} | "
            f"Assigned Enclosures: {len(self.__assigned_enclosures)}"
        )


# -----------------------------
# Zookeeper class
# -----------------------------

class Zookeeper(Staff):
    """Zookeepers feed animals and clea  enclosures"""
    def get_role(self):
        return "Zookeeper"

    def feed_animal(self, animal):
        """feed an assigned animal"""
        if (animal in self.assigned_animals or
                animal.get_enclosure() in self.assigned_enclosures):
            return (
                f"{self.name} fed {animal.name()}."
                f"Result: {animal.eat()}"
            )
        return f"{self.name} is not assigned to {animal.name()}"

    def clean_enclosure(self, enclosure):
        """clean an assigned enclosure"""
        if enclosure in self.assigned_enclosures:
            enclosure.clean()
            return (
                f"{self.name} cleaned {enclosure.name}. "
                f"Cleanliness is now {enclosure.cleanliness_level}%."
            )

        return f"{self.name} is not assigned to {enclosure.name}"


# -----------------------------
# Veterinarian class
# -----------------------------
class Veterinarian(Staff):
    """Vets perform health checks and treatments"""
    def get_role(self):
        return "Veterinarian"

    def conduct_health_check(self, animal):
        """Conduct a health check on an assigned animal"""
        if animal in self.assigned_animals:
            status = (
                "has active health issues"
                if animal.has_active_health_issues()
                else "is healthy"
            )
            return (
                f"{self.name} examined {animal.name()}. "
                f"{animal.name()} {status}."
            )
        return f"{self.name} is not assigned to {animal.name()}"

    def treat_animal(self, animal, record):
        """Treat an animal for a health issue"""
        if animal not in self.assigned_animals:
            return f"{self.name} is not assigned to {animal.name()}"

        if record not in animal.health_records():
            return f"Record not found for {animal.name()}"

        if record.resolve:
            return f"This issue is already resolved."

            # Resolve the issue
        record.resolve()
        return (
            f"{self.name} treated {animal.name()} for: "
            f"{record.description()}"
        )