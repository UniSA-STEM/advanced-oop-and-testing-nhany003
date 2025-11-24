'''
File: main.py
Description: This Python modul acts as a demostration script,
demonstrating the use of the defined classes (Animal, Enclosure and Staff).
Author: Nenciliae Nhanga
ID: 110100110
Username: NHANY003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Mammal, Reptile, Bird, HealthRecord, Severity
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian
from datetime import date

# -------------------
# Create Enclosures
# -------------------
print("\n--- Create enclosure ---")
savannah = Enclosure("African Savannah", 5000, "Savannah", 5)
print(f"Created: {savannah}")

reptile_house = Enclosure("Reptile House", 800, "Desert", 8)
print(f"Created: {reptile_house}")

aviary = Enclosure("Tropical Aviary", 1200, "Tropical", 10)
print(f"Created: {aviary}")

aquatic_zone = Enclosure("Aquatic Zone", 3000, "Aquatic", 6)
print(f"Created: {aquatic_zone}")

# -------------------
# Create Animals
# -------------------
print("\n--- Creating animals  ---")
# Mammals

Marty = Mammal("Marty", "Zebra", 3, "Grass")
Marty.enclosure = savannah
print(f"Created: {Marty}")

Horton = Mammal("Horton", "Elephant", 12, "Hay and vegetables")
Horton.enclosure = savannah
print(f"Created: {Horton}")

# Reptiles
Steve = Reptile("Steve", "Python", 7, "Rodents", is_venomous=False)
Steve.enclosure = reptile_house
print(f"Created: {Steve} - Venomous: {Steve.is_venomous}")

Allan = Reptile("Allan", "King Cobra", 4, "Small mammals", is_venomous=True)
Allan.enclosure = reptile_house
print(f"Created: {Allan} - Venomous: {Allan.is_venomous}")

# Birds
Polly = Bird("Polly", "Parrot", 2, "Seeds and fruits", can_fly=True)
Polly.enclosure = aviary
print(f"Created: {Polly} - Can fly: {Polly.can_fly}")

Mumble= Bird("Mumble", "Penguin", 3, "Fish", can_fly=False)
Mumble.enclosure = aquatic_zone
print(f"Created: {Mumble} - Can fly: {Mumble.can_fly}")

# -------------------
# Demonstrate animal behaviours
# -------------------
print("\n--- Animal behaviours ---")
print(Steve.sleep())
print(Marty.eat())
print(Horton.make_sound())

# -------------------
# Add Animals to Enclosures
# -------------------
print("\n--- Animals added to enclosure ---")
savannah.add_animal(Horton)
savannah.add_animal(Polly)  # Should fail - different species
reptile_house.add_animal(Steve)
aviary.add_animal(Mumble)

# -------------------
# Create Staff
# -------------------
print("\n--- Creating Staff ---")
zookeeper_Addy = Zookeeper(name="Addy", employee_id=101)
zookeeper_Addy.assign_enclosure(savannah)
zookeeper_Addy.assign_enclosure(aquatic_zone)

veterinarian_Alice = Veterinarian(name="Alice", employee_id=201)
veterinarian_Alice.assign_animal(Mumble)
veterinarian_Alice.assign_animal(Horton)

# -------------------
# Staff Actions
# -------------------
print("\n--- Staff actions ---")
print(zookeeper_Addy.feed_animal(Horton))
print(zookeeper_Addy.clean_enclosure(savannah))
print(veterinarian_Alice.conduct_health_check(Mumble))
print(veterinarian_Alice.get_role())

# -------------------
# Health Records
# -------------------
print(veterinarian_Alice.conduct_health_check(Marty))

print("\n--- Adding Health Record ---")
Marty_injury = HealthRecord(
    description="Minor leg injury",
    severity=Severity.LOW,
    treatment_plan="Clean wound daily",
    date_reported=date.today(),
)
Marty.add_health_record(Marty_injury)
print(f"Health record added for Marty")
print(f"Marty under treatment: {Marty.under_treatment}")
print(f"Can Marty be moved? {Marty.can_be_moved()}")

print("\n--- Treating Marty ---")
print(veterinarian_Alice.treat_animal(Marty, Marty_injury))
print(f"Marty under treatment: {Marty.under_treatment}")


# -------------------
# Display Enclosure Status
# -------------------
print(savannah.get_status())



