^^^^#LINK :
#  https://www.w3resource.com/python-exercises/python-basic-exercises.php

#1
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\tUp above the world so high,\n\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")
# \n   es un enter
#\t es un indent


#2
import sys
print("Python version")
print(sys.version)


#3
import datetime
now = datetime.datetime.now()
print(" Date & Time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


#4
import math
radius = float(input("Enter a Radius Value: "))
# AREA = PI * RADIUS ^2
area_circle = radius**2 * math.pi
print("The Area of a circle with Radius =" +str(radius) + "is =" + str(area_circle))

print("\n")


#5
first_name = input("Enter you´r first name:")
last_name = input("Enter you´r last name:")
print("You´r new name is:" +last_name +" "+ first_name)

#6
sample_data = input("Enter the data of numbers (no comas): ")
print("list:" + list(sample_data))
print("tuple:" + tuple(sample_data))

#7     ''' str.split () '''
print("\n")
sample_file = input("Type in a file name:" )
file_extension = sample_file.split(".")
print("You´r file extension is:" + str(file_extension[1]))

#8
color_list = ["Red","Green","White" ,"Black"]
print("your 1st and last color´s are:" + color_list[0]  +  color_list[3])

#9
exam_st_date = (11, 12, 2014)
print("The examn is the day %i/%i/%i"%exam_st_date)


#10    '''accepts an integer (n) and computes the value of n+nn+nnn'''
integer_input = input("Enter any integer n =")
integer_float = float(integer_input)
expected_results = integer_float + integer_float**2 + integer_float**3
print("you´r expected results are = " + str(expected_results))

# other way... not multiplying.

integer_input = input("Enter any integer n =")
n1 = int("%s"%integer_input)
n2 = int("%s%s"%(integer_input,integer_input))
n3 = int("%s%s%s"% (integer_input, integer_input, integer_input))

print(n1+n2+n3)

#11
print(abs.__doc__)

#12
import calendar
year = int(input("Enter a Year: "))
month = int(input("Enter a Month: "))
print(calendar.month(year, month))


#13
print("""a string that you\"don't\"have to escape
This is a .....multi-line 
heredoc string----> example""")

#14
#number of days between two days
import datetime
date_1 = datetime.date(2017, 4, 4)
date_2 = datetime.date(2017, 5, 8)
print(date_2 - date_1)


#15
#formula = Vol = 4/3 * pi * r^3
import math
radius = 6
volume = (4/3) * math.pi * radius**3
print(volume)

#16
def differences(n):
    if n > 17:
        return n-17
    else:
        return abs((n-17)*2)

differences(14)

#17
#if it is in a range...
def range_numbrs(n):
    if n <= 1000:
        return "Yes"
    elif n <= 2000:
        return "YES"
    else:
        return "Nop"

range_numbrs(2001)

#if it is close to a number:
def near_a_thousand(n):
    if abs(1000-n) <= 100 or abs(2000-n)<= 100:
        return True
    else:
        return False
    
near_a_thousand(800)



#18
def function_ej18(n1, n2, n3):
    if n1 != n2 or n2 != n3 or n1 != n3:
        print(n1 + n2 + n3)
    else:
        print(n1 *3**2)
function_ej18(2,2,2)

#19
"""
string_origin = "a cat in the hat"
new_str = "Is " + string_origin
print(new_str)
"""
def new_string(str):
    if str[0:2]== "Is":
        return str
    else:
        return "Is " + str
    
new_string("Is Apenddd")

"""
tester_str = "Hello World"
if tester_str[0] == "H" :
    print(True)
else:
    print(False)
"""

#20
def new_string(n,str):
    print(n*str)
new_string(5,"I am, ")

#21
even_odd = input("Enter a num: ")
if int(even_odd) % 2 == 0:
    print("you´r num is even !")
else:
    print("you´r num is odd...")


#print( 5 % 2) =  2 remeinder 1
    
    
    
#22    
list_1 = [1, 2, 3, 4, 5, 6 ,7, 1, 0, 4, 6, 7, 4]
list_1.count(4)

#24

def vowel_machinee(character):
    all_vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if character in all_vowels:
        print("it´s a vowel !")
    else:
        print("you´r letter isn´t a vowel...")

vowel_machinee("A")


#25
list_of_values_to_check = [0, 1, 2, 3, 4, 5, 6, 9, 10]
value_to_check = input("Enter a value to check: ")

if int(value_to_check) in list_of_values_to_check:
    print("You´r value is in the list !")
else:
    print("You´r value is not in the list...")


#26
def histogram( items ):
    for i in items:
        output = ''
        times = i
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)
histogram([2, 3, 6, 5])


#27
def concatenator(list):
    result = ''
    for i in list:
        result += str(i)
    print (result)

concatenator([0,1,2,3,4,])

#28

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]

for i in numbers:
    if i % 2 == 0:
        print(i)
    elif i == 237:
        break


#29
        
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

for i in color_list_1:
    if not i in color_list_2:
        print(i)
        


#30 
base = input("Enter a base of your triangle: ")
height = input("Enter a hight of your triangle: ")
area = 0.5*int(base)*int(height)
print(str(area) +"cm^2")


#33

number1 = input("Enter your 1st number:")
number2 = input("Enter your 2nd number:")
suma = int(number1) + int(number2)
if number1 == number2:
    suma = 0
    print(suma)
else:
    print(suma)

#34  

number1 = input("Enter your 1st number:")
number2 = input("Enter your 2nd number:")
suma = int(number1) + int(number2)
if suma in [15,20]:
    suma = 20
    print(suma)
else:
    print(suma)


#35
def tester_conditions(x, y):
    if x == y or abs(x - y)==5 or (x+y)==5:
        print("cumple!")
    else:
        print("Don´t")

print(tester_conditions(2,2))


#36
#The isinstance() function returns True if the specified object is of the specified type

def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
         raise TypeError("Inputs must be integers")
    return a + b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(add_numbers(a, b))

#37
def personal_data():
    name, age, adress = "Jerry", 20, "33 Oriental's"
    print("name: {} \nAge: {} \nAdress: {}".format(name, age, adress))

personal_data()


#38
x = 4
y = 3
formula = "(x+y)^2 = "
results = (x+y)**2
print(formula + str(results))








#39

#compute the future value of a specified principal amount, rate of interest, and a number of years.
#Test Data : amt = 10000, int = 3.5%, years = 7

principal = 10000
ints = 3.5/100 #because it´s 3.5%
yrs = 7
future_value = print(principal*(1+ints)**yrs)



#40
# distance between two points = P(x1,y1) and Q(x2,y2) is given by: d(P, Q) = √ (x2 − x1)2 + (y2 − y1)2
import math
def distance():
    p1 = [1,2]
    p2 = [5,6]
    print(math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2))

distance()



#42
#get OS name, platform and release
import platform
import os
print(os.name)
print(platform.system())
print(platform.release())



#43
print(os.name)
print(platform.system())
print(platform.release())

#44 locate site packages      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
import site
print(site.getsitepackages())


#46 get the path and name of the file that is currently executing
import os
print("Current File Name : ",os.path.realpath(__file__))

#59   Inch to cm converter

inches = input("Enter inches: ")
cms = float(inches) * 2.54
print("That´s " +str(cms) + " cm's !")

# foot to cm converter
feet = input("Enter your height in feet: ")
inches = float(feet)*12
cms = float(inches) * 2.54
print("That´s " + str(cms) + " cm´s  or " + str(cms/100) + " meters !")


#60 
from math import sqrt 
side_a = input("enter side a´s length: ")
side_b = input("enter side b´s length: ")
# H ^2 = a ^2 + b ^2
hypotenuse = sqrt(int(side_a)**2 + int(side_b)**2)
print(hypotenuse)




# 66
#BMI = W / H^2     if height in m weight in kg    if height in feet weight in lb
weight = float(input("Enter weight: "))
height = float(input("Enter height: "))
bmi = weight / height**2
print("Your BMI = " + str(bmi) )

#67
preasure_kilopascals = input("Enter preasure in pascals:")
pounds_x_sqrinch = 0.145030 * int(preasure_kilopascals)
print("That´s {} pounds per square inch.".format(round(pounds_x_sqrinch,3)))
milimeter_mercury = 7.50062 * int(preasure_kilopascals)
print("That´s {} mmHg".format(round(milimeter_mercury,3)))
atmosphere_preasure = 0.00986923 * int(preasure_kilopascals)
print("That´s {} units of atmosphere preasure.".format(round(atmosphere_preasure,3)))


#68  // divide with int results (descard remainder)
#example:
number = int(123)
print(number // 100)

def sum_of_digits():
    number = int(input("Enter a 4 digit number: "))
    x1 = number // 1000
    x2 = (number - x1*1000) // 100
    x3 = (number - x1*1000 - x2 * 100) // 10
    x4 = (number - x1*1000 - x2 * 100 - x3 * 10 )
    print("sum of all it´s digits = " + str( x1 + x2 + x3 + x4))

sum_of_digits()


#69
num1 = 6
num2 = 4
num3 = 8

first_num = max(num1, num2, num3)
last_num = min(num1, num2, num3)
middle = (num1+num2+num3)-first_num - last_num
print("the numbers in order are : " , first_num, middle, last_num)


#73
point1 = (10937, 847123)
point2 = (432341, 3414)
midpoint = print("("+str(point1[0]/2 + point2[0]/2),",",str(point1[1]/2 + point2[1]/2)+")")


#74    HASH OF A WORD ???
soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
 
word=input("Input the word be hashed: ")
 
word=word.upper()

coded=word[0]
 
for a in word[1:len(word)]:
    i=65-ord(a)
    coded=coded+str(soundex[i])
print() 
print("The coded word is: "+coded)
print()

?ord

#78 FIND HOW MANY BUILT IN MODULES ARE AVAILABLE
import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))



#79
#import sys
str1 = "Hello i´m Jerry"
print("Memory size of \""+ str1 + "\" is "  + str(sys.getsizeof(str1)) + " bytes")



















