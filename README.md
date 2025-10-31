# Summary<br>
This is a random npc genertaor using all the basic fundamentals of python. It utilizes; lists, conditionals, loops, booleans, integers, strings, variables, user input, print statements, python libraries, python functions, and other basic python know how. The goal is for it be presented in a professional way to be suitable for a client. It is extremely intuitive and simple to use but uses some cool tricks to add vareity behind the scenes. 

## How It Works<br>
In order for organization this section of the readme will mostly describe the code from top to bottom.<br>
The program begins with importing the two libraries nescesary; time and random.<br> 
Next is the first user input of the progam which asks the number of NPCs desired, this will be essential later on.<br>
The lists of the atributes are all next, there are total of 4 lists in order to add a wide range variety for each NPC, these lists are; gender, personality, physical characteristics, and occupations.<br>
After the lists begins the loop, which is most of the code and all of the logic take place.<br>
The loop is in a "for" format using the range for the number of repeats from the user input at the very beggining.<br>
The first line in the loop is a print statment that is there only for cosmetic purposes and will be used along side the next user input.<br>
Next this section of the loop is dedicated to the generation of the characters height. This uses a random.uniform function to pick between a range of floats. These which ever height is then selected for the NPC then decides its subsequent race. This is done by using if statements to assign the race variable equal to a string with it's name. For example elfs are any height betwen 6.2 and 7.2.<br>
The next part is to determine where the character lives. This is done by assigning the variable "living_space" to either randomly true or false. If it equals true they live in the country and if else the city.<br>
The next part utilizes the race identified in the previous part in order to generate the age. For instance if the race is a dwarf, it will choose a random integer between 18 and 220. This is just using simple conditional statements.<br>


