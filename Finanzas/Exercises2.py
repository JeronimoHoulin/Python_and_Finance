# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:32:02 2020

@author: jeron
"""
#https://www.w3resource.com/python-exercises/basic/


#1

print(set("python"))

def same_tester (sequence):
    if len(sequence) == len(set(sequence)):
        return True
    else:
        return False


sequence = [1,2,3,4,4, 5, 6]
same_tester(sequence)


#2 
#basic idea
import random
vowel_list = ['a', 'e', 'i', 'o', 'u']
random.shuffle(vowel_list)
print(''.join(vowel_list))
#function 
vowel_list =['a', 'e', 'i', 'o', 'u']
def all_posible_strs(vowel_list):
    listy = []
    while len(listy) != 120:
        random.shuffle(vowel_list)
        x = [''.join(vowel_list)]
        if x not in listy:
            listy.append(x)
        else:
            print("Combination already in list !")
    
    return listy
    print("All combinations created !")

all_posible_strs(vowel_list)





#3
lista = [1, 2, 3, 4, 5, 6, 7, 8]
#testing out
lista.pop(2)
print(lista)
len(lista)

#function
def remover(lista):
    while len(lista) > 2:
        lista.pop(2)
    else:
        print("The list is now in the two last nums:" + str(lista))
        lista.pop(1)
        lista.pop(0)
        print(lista)
        print("lista vacía !")
    

remover(lista)


#4

#5
from itertools import permutations
permutations([1, 2, 3])
list(permutations([1, 2, 3]))

#and

for perms in permutations([1, 2, 3]):
    print(perms)
    

#6
string_words = "Hello World, Fuck The Police !"





#8. Write a Python program to get the top stories from Google news !!!

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url="https://news.google.com/news/rss"   #la calve acá es sacar el XML de la pagina de noticias
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
  print(news.title.text)
  print(news.link.text)
  print(news.pubDate.text)
  print("-"*60)


#9 Locally installed packages
import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
for m in installed_packages_list:
    print(m)


#18 La mediana de una lista
lista = [1, 2, 3, 4, 5, 6, 7, 8] #mediana = 4
if len(lista)/2 - int(len(lista)/2) != 0:      #caso fácil, lista NO entera ó if len(lista)% 2 !=0
    mid_pos = int(len(lista)/2)                #int() redondea para abajo pero como la lista 
    print(lista[mid_pos])                      #está indexada 0 está bien

else:
    mid_pos_2 = []
    mid_pos_2.append(int(len(lista)/2))        #caso jodido.. par
    mid_pos_2.append(round(len(lista)/2 +1, 0))
    print(mid_pos_2)
    mid_pos_ = (mid_pos_2[0] + mid_pos_2[1])/2
    print(round(mid_pos_,6))




if len(lista)% 2 == 0:
    print(True)




###### random exercise of ZIP ######
animals = ["Panda", "Gorila", "Griaff", "Elefant", "Horse", "Duck", "Lion", "Snake"]
quantity = [5, 8, 2, 9, 12, 2, 6, 9]
#zip
base_datos = list(zip(animals, quantity))
print(base_datos)
#un zip
animales, cantidad = zip(*base_datos)
print(animales)
print(cantidad)
#list
for i, j in zip(range(len(animales)), animales):
    print(i,j)


#la idea de enumerar una lista... medio gede
x = range(len(quantity))
print(list(x))




#32
height_buildings = [2398, 1345, 4251, 1245, 9969, 3567, 1675, 2476, 3246, 8355, 5754, 7975] 

heighest = []
while len(heighest) < 3:
    x = max(height_buildings)
    heighest.append(x)
    height_buildings.remove(x)
    
print(heighest)


#35
#Write a Python program to compute the amount of the debt in n months. 
#The borrowing amount is $100,000 and the loan adds 5% interest of the debt
# and rounds it to the nearest 1,000 above month by month.

n_months = int(input("Enter amount of month´s you want to borrow $100k for: "))
int_rate = 0.05
borrow = 100000
debt_amount = round(borrow *(1+int_rate)**n_months, 1000)
print("In {} month´s you will owe: $".format(n_months) + str(round(debt_amount,2)))

    


#38
less_than = 20
print("All prime numbers less than or equal to {}".format(less_than))
for num in range(0,less_than +1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)



#42

def descending (numbers):
    list_desc = []
    length = len(numbers)
    while len(list_desc) != length:
        for i in numbers:
            if i == max(numbers):
                list_desc.append(i)
                numbers.remove(i)
    else:
        print(list_desc)
        
numbers = [10, 47, 41, 69, 42, 58, 14, 93, 1034]
descending(numbers)


























