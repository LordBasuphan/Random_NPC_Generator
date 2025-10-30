import random 

#User input- input from user for certian aspects of the program
number_of = int(input("How many would you like to create:"))

#Atrribute lists- list of all the atributes needed
gender_list = ["male", "female", "non-binary"]

personality_list = ["Confident", "Ambitious", "Calm", "Courageous", "Creative", "Adaptable", "Humble", "Cheerful", "Curious", "Patient", "Analytical", "Agreeable", "Adventurous","Loyal", "Compassionate", "Imaganitive", "Affectionate", "Capable"]

physical_list = ["Ugly", "Fat", "Scrawny", "Weak", "Strong", "Handsome", "Pretty", "Petite", "Athletic", "Hairy", "Bald", "Long-haired", "Short-haried", "Slender", "Stocky"]

occupation_list = ["Bard", "Theif", "Chemist", "Hunter", "Mage", "Alchemist", "Cleric", "Diplomat", "Investigator", "Knight", "Archer", "Cook", "Wizard"]
    
#Loops/Print
for i in range(number_of):
    #Height/Race- function to determine the height and then subsequent race of each character
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
#Age, algorithm to determine the age of a npc
    age = 0
    if race == "Human":
        age = random.randrange(18,100)
    elif race == "Elf":
        age = random.randrange(18,150)
    elif race == "Dwarf":
        age = random.randrange(18,220)
    name = input("Provide a name for the NPC:")
    print(f"{name} is a",random.choice(physical_list).lower() + " and",random.choice(personality_list).lower(),random.choice(gender_list) + " " + race + "." + " They are a", random.choice(occupation_list).lower() + " and are", str(rounded_height) + " feet tall.")
