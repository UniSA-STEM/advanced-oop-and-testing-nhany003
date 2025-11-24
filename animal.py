'''
File: filename.py
Description: A brief description of this Python module.
Author: Nenciliae Nhanga
ID: 110424563
Username: nhany003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from datetime import date
from typing import List


class HealthRecord:
    def __init__(self, description, severity, treatment_plan, date_reported):
        self.__description = description
        self.__date_reported = date_reported
        self.__severity = severity
        self.__treatment_plan = treatment_plan
        self.__resolved = False

    """ Set to private to ensure all data entered is valid"""

    @property
    def description(self):
        return self.__description

    @property
    def date_reported(self):
        return self.__date_reported

    @property
    def severity(self):
        return self.__severity

    @property
    def treatment_plan(self):
        return self.__treatment_plan

    @property
    def resolved(self):
        return self.__resolved

    def resolve(self):
        self.__resolved = True

    def update_treatment(self, new_plan):
        self.__treatment_plan = new_plan

    def __str__(self):
        status = "Resolved" if self.resolved else "Active"
        sev = self.severity.value if hasattr(self.severity, "value") else self.severity
        return (f"[{status}] {sev} - {self.description} "
                f"(Reported: {self.date_reported.strftime('%Y-%m-%d')})")


class Animal:

    def __init__(self, name, species, age, dietary_needs):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = dietary_needs
        self.__health_records: List[HealthRecord] = []
        self.__under_treatment = False
        self.__enclosure = None

    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species

    @property
    def age(self):
        return self.__age

    @property
    def dietary_needs(self):
        return self.__dietary_needs

    @property
    def health_records(self):
        return self.__health_records

    @property
    def enclosure(self):
        return self.__enclosure

    @property
    def under_treatment(self):
        return self.__under_treatment

    # --------------------
    # Setters
    # --------------------

    @name.setter
    def name(self, name):
        if not name or len(name.strip()) == 0:
            raise ValueError("Name cannot be empty")
        self.__name = name

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.__age = age

    @dietary_needs.setter
    def dietary_needs(self, dietary_needs):
        if not dietary_needs:
            raise ValueError("Dietary needs cannot be empty")
        self.__dietary_needs = dietary_needs

    @enclosure.setter
    def enclosure(self, enclosure):
        """Assign animal to an enclosure.
        Validates that the animal can be moved and the enclosure is suitable.
        """
        # Allow setting to None (removing from enclosure)
        if enclosure is None:
            self.__enclosure = None
            return

        # Validate enclosure type
        # Check if animal can be moved (not under treatment)
        if self.__under_treatment:
            raise ValueError(
                f"Cannot move {self.__name} to enclosure: animal is currently under treatment. "
            )
        # Check if enclosure has capacity
        if enclosure.is_at_capacity:
            raise ValueError(f"Cannot assign {self.__name}: enclosure is at capacity.")

        # Check if enclosure is suitable for species
        if enclosure.allowed_species is not None and enclosure.allowed_species != self.__species:
            raise ValueError(
                f"Enclosure already houses species: {enclosure.allowed_species}."
            )

        # If all validations pass, assign the enclosure
        self.__enclosure = enclosure

    # ----------------------
    # Core methods
    # ----------------------
    def make_sound(self):
        return f"{self.__name} the {self.__species} is making a sound"

    def eat(self):
        return f"{self.__name} is eating {self.__dietary_needs}"

    def sleep(self):
        return f"{self.__name} is sleeping"

    # Health Management
    def add_health_record(self, record: HealthRecord):
        """Add a new health record and update treatment status."""
        self.__health_records.append(record)
        # Automatically update treatment status
        self.__update_treatment_status()

    def has_active_health_issues(self):
        """return true if any health record is not resolved."""
        return any(not record.resolved for record in self.__health_records)

    def __update_treatment_status(self):
        """Check if any health record is still active (not resolved)"""
        self.__under_treatment = any(not record.resolved for record in self.__health_records)

    def can_be_moved(self):
        """Check if animal can be moved between enclosures.
        Animals under treatment should not be moved."""
        return not self.__under_treatment

    def generate_health_report(self):
        """create a detailed health report for this animal."""
        report = f"Health Report for {self.__name} ({self.__species})\n"
        report += f"Age: {self.__age} years\n"
        report += f"Dietary Needs: {self.__dietary_needs}\n"
        report += f"Current Enclosure: {self.__enclosure if self.__enclosure else 'Not assigned'}\n"
        report += f"Treatment Status: {'Under Treatment' if self.__under_treatment else 'Healthy'}\n"
        return report

    def __str__(self):
        status = " [Under Treatment]" if self.__under_treatment else ""
        return f"{self.__name} ({self.__species}, {self.__age} years){status}"


# Mammal subclass
class Mammal(Animal):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)

    def make_sound(self):
        return f"{self.name()} makes a mammal sound"


# Reptile subclass
class Reptile(Animal):
    def __init__(self, name, species, age, dietary_needs, is_venomous=False):
        super().__init__(name, species, age, dietary_needs)
        self.__is_venomous = is_venomous

    def make_sound(self):
        return f"{self.name()} makes a reptile sound"

    @property
    def is_venomous(self):
        return self.__is_venomous


# Bird subclass
class Bird(Animal):
    def __init__(self, name, species, age, dietary_needs, can_fly=True):
        super().__init__(name, species, age, dietary_needs)
        self.__can_fly = can_fly

    @property
    def can_fly(self):
        return self.__can_fly

    def make_sound(self):
        return f"{self.name()} makes a bird sound"
