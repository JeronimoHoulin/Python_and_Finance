print("\n")


# 1hra 10min
# DEF START OF FUNCTION HEADER
def say_hi(name, age):
    print("Hello " + name + ", you'r " + str(age))


print("top")
say_hi("Mike", 15)
say_hi("Steve", 43)
print("bottom")
print("\n")


# 1hra 34min
# RETURN STATEMENT
def cube(num):
    return num * num * num


print(cube(4))
print("\n")

# 1hra 40min
# IF STATEMENTS
is_male = False
is_tall = False
if is_male and is_tall:
    print("You are Tall Male.")
elif is_male and not (is_tall):
    print("You are male, BUT you are NOT tall.")
elif not (is_male) and is_tall:
    print("Your are Tall, but not Male.")
else:
    print("You are neither tall NOR male.")
print("\n")


# 1hr54min
# COMPARISONS IN IF STATEMENTS
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(num1 + " is the largest number.")
    elif num2 >= num1 and num2 >= num3:
        print(num2 + " is the largest number.")
    else:
        return num3
print(max_num(3, 4, 5))
print("\n")

#2hrs 00min
# BUILDING A CALCULATOR
'''
num1 = float(input("Enter first number: "))
op = input("Enter an operator: ") # sumar, multiplicar....
num2 = float(input("Enter second number: "))
if op == "+":
  print(num1+num2)
elif op == "-":
   print(num1 - num2)
elif op== "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Not a valid operator")
'''
print("\n")

#2hrs 07min
# DICTIONARIES  ( WORD / KEY   ;   DEFINITION / VALUE)
MonthConversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun": "June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}
print(MonthConversions.get("Jul", "Not a valid month"))
print("\n")
#2hrs 15min
# WHILE LOOP
#first thing is create an integer
i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with loop.")
print("\n")

#2hrs 20min
# Guessing Game
secret_word = "Jerry"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
   print("Out of guesses...")
else:
   print("You guessed it !")
print("\n")

#2hrs 32min
# FOR LOOPS
# for variable in collection:
for letter in "Jerry´s skils":
    print(letter)
#for loop´s for every iteration in the collection
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)
for index in range(10,20,2):
    print(str(index))
print("\n")

#2hrs 41min
#EXPONENT FUNCTION
print(3**2)
#using for loops
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num): #the amount of times that the loop is made = pow_num
        result = result * base_num
    return  result
print(raise_to_power(3, 24))
print("\n")
#2hrs 47 min
#2D LISTS & NESTED LOOPS
number_grid =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
    ]# list inside a list = "GRID"
#print(number_grid[2][1]) #rows and columns (in that order) arre zero indexed
#nested for loop (for loop in a for loop)
for row in number_grid:
    for col in row:
        print(col)
print("\n")

#2hrs 52min
#TRANSLATOR
# all vauels ==>> "g"
def translate (phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": # or "if letter.lower() in "aeiou""
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))
print("\n")

#3hrs 02min
#TRY ; EXCEPT   (CATCHING ERRORS)
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("invalid input")
print("\n")

#3hrs 12 min
# READING FILES
employee_file = open("Nombres de empleados.txt", "a") # mode "r" = read ; "W" = write (overwright everything) ; "a" = appende (add new info) ; "r+" (read & write)
#check if the file is readable: ("True = readable") (if mode = "W" then readable = F)
#print(employee_file.readable())
#print(employee_file.read())
#print(employee_file.readline())        #line or lines
#print(employee_file.readlines()[1])    #indexed 0
#always close file after using:



#3hrs 21min
# WRITING TO FILES and appending to existing files
employee_file.write("Toby - Recursos Humanos")

employee_file.close()
#muchas más mañas de crear nuevos archivos y demás min y 27...
print("\n")

#3hrs 28min
# MODULES AND PIP
'''
import #name of the other file with usefull functions
print(useful_tools.#function)

in google; list of python modules in python, official page.
# Python docx ; on command prompt ; "   pip insatall python-docx   " ==> lib ; site-packages
" External libraries ; Lib ; xmlrpc ; all tipes of modules
'''
#3hrs 44min
# CLASSES & OBJECTS (creating data tipes)
'''
in a file:  Class / template
'''
class Student: #defining what a student is in this program
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
'''
On this file, to access the file "from Student import Student":
  Object :
'''

student1 = Student("Jim", "Business", 3.1, False)
print(student1.name)
print("\n")

#3hrs 57min
# MULTIPLE CHOICE QUESTIONS
question_prompt = ["What is my name?\n(a) Martin\n(b) Jerry\n(c) Tom\n\n",
                    "What is my dog´s name ?\n(a) Medias\n(b) Luis\n(c) Tim\n\n"]
# create a class
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question(question_prompt[0],"b"),
    Question(question_prompt[1], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print ("You got " + str(score) + " answers right")
run_test(questions)
print("\n")

#4hrs 8min
#OBJECT FUNCTIONS
"""
class Alumno:
    def __init__(self, name, major, gpa):     #sefl. is the actual students data
        self.name= name
        self.mjaor= major
        self.gpa= gpa
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
"""
from Students import Student

person1 = Student("Oscar", "Accounting", 3.1)
person2 = Student("Phyllis", "Business", 3.8)

print(person1.on_honor_roll())
print("\n")

#4hrs 13min
# INHERITANCE
from Chef import TheChef
myChef = TheChef()
myChef.make_special_dish()

class ChineaseChef(TheChef):   #INHERETED
    def make_fried_rice(self):
        print("Chinease Chef makes fried rice")
    def make_special_dish(self):  #to NOT inheret the same "make_special_dish
        print("The Chinease Chef makes Oragne Chicken")

MyChiChef = ChineaseChef()

MyChiChef.make_special_dish()

print("\n")

#4hrs 23min
# PYTHON INTERPRETER
#IN COMMAND PROMPT
"""
Enter "cmd" un search to open comand prompt
tipe in "python" hit enter
see version of python....... OK !
"""
