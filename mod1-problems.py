# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."

print('Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.')

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.

num1 = int(input('Type in a whole number. '))
num2 = int(input('Type in another whole number. '))

print(num1,' + ',num2,' = ',num1+num2)
print(num1,' - ',num2,' = ',num1-num2)
print(num1,' x ',num2,' = ',num1*num2)
print(num1,' / ',num2,' = ',num1/num2)

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)

tri1 = float(input('Give the first side length of a triangle: '))
tri2 = float(input('Give the second side length of a tria3ngle: '))
tri3 = float(input('Give the third side length of a triangle: '))

sper = (tri1 + tri2 + tri3) / 2

import math
area = math.sqrt(sper * (sper - tri1) * (sper - tri2) * (sper - tri3))

print('The area of the triangle is: ',area)


# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).

num1 = int(input('You will be asked to provide 5 numbers, please input the first number: '))
num2 = int(input('Second number: '))
num3 = int(input('Third number: '))
num4 = int(input('Fourth number: '))
num5 = int(input('Fifth number: '))

#https://www.geeksforgeeks.org/python-program-to-find-smallest-number-in-a-list/
list = [num1, num2, num3, num4, num5]

total = num1+num2+num3+num4+num5
mean = total/5

#SD Calculation
sd1 = (num1 - mean)**2
sd2 = (num2 - mean)**2
sd3 = (num3 - mean)**2
sd4 = (num4 - mean)**2
sd5 = (num5 - mean)**2
sdsolve = float((sd1+sd2+sd3+sd4+sd5)/4)


print('Total is: ', total)
print('Average is: ', mean)
print('Minimum is: ', min(list))
print('Maximum is: ', max(list))
print('Range is: ', min(list) - max(list))
print('SD is: ', sdsolve)
