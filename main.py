import random 
gender_list = ["male", "female", "non-binary"]

personality_list = ["Confident", "Ambitious", "Calm", "Courageous", "Creative", "Adaptable", "Humble", "Cheerful", "Curious", "Patient", "Analytical", "Agreeable", "Adventurous","Loyal", "Compassionate", "Imaganitive", "Affectionate", "Capable"]

height = random.uniform(2.0,7.0)
rounded_height = round(height, 2)
#use rounded_height as the main variable for this
print(rounded_height)

race = ""
if rounded_height >= 5.0:
    race = "Human"
elif rounded_height >= 6.3:
    race = "Elf"
elif rounded_height <= 5 and rounded_height >= 2:
    race = "Dwarf" 

print(race)