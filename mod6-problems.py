#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.

lista = [1,2,3,4,5]
listacount = len(lista)
count = 0
sum = 0

while count < listacount:
    sum += lista[count]
    count += 1
print(sum)

#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.

listb = ['Olympic', 'Apple', 'Olympic']
listbcount = len(listb)
count = 0
sum = 0

while count < listbcount:
    if listb[count] == 'Olympic':
        sum += 1
    count += 1
print(sum)

#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.

listc = ['Tree','Apple','Orange','a','Two','Bridge']
listccount = len(listc)
count = 0

while count < listccount:
    if len(listc[count]) <= 3:
        del listc[count]
        listccount -= 1
        count -= 1
    count += 1
print(listc)

#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.

listd = [1,-2,3,4,-5]
listdcount = len(listd)
count = 0
pos = 0
neg = 0

while count < listdcount:
    if listd[count] < 0:
        neg += 1
    else:
        pos += 1
    count += 1
print('There are ',pos,' positive numbers and ',neg,' negative numbers.')

#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.

import math
liste = [4,16,25]
listecount = len(liste)
count = 0

while count < listecount:
    liste[count] = math.sqrt(liste[count])
    count += 1
print(liste)
