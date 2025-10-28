import random 

#User input
# name = input("Enter a name for your character:")

# number_of = int(input("How many would you like to create:"))

#Atrribute lists
gender_list = ["male", "female", "non-binary"]

personality_list = ["Confident", "Ambitious", "Calm", "Courageous", "Creative", "Adaptable", "Humble", "Cheerful", "Curious", "Patient", "Analytical", "Agreeable", "Adventurous","Loyal", "Compassionate", "Imaganitive", "Affectionate", "Capable"]

physical_list = ["Ugly", "Fat", "Scrawny", "Weak", "Strong", "Handsome", "Pretty", "Petite", "Athletic", "Hairy", "Bald", "Long-haired", "Short-haried", "Slender", "Stocky"]

occupation_list = ["Bard", "Theif", "Chemist", "Hunter", "Mage", "Alchemist", "Cleric", "Diplomat", "Investigator", "Knight", "Archer", "Cook", "Wizard"]



#Height/Race
height = random.uniform(3.0,7.2)
rounded_height = round(height, 2)
#use rounded_height as the main variable for this
race = ""
if rounded_height >= 5.0:
    race = "Human"
elif rounded_height >= 6.3:
    race = "Elf"
elif rounded_height <= 5 and rounded_height >= 3.0:
    race = "Dwarf" 
print(race)

#Age
age = 0
if race == "Human":
    age = random.randrange(18,100)
elif race == "Elf":
    age = random.randrange(18,150)
elif race == "Dwarf":
    age = random.randrange(18,220)
print(age)