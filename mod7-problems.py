
'''
#1. Write a function called count_vowels(input) that takes a string
and returns the number of vowels (a, e, i, o, u) in it.
'''
def count_vowels(input):
    count = 0
    for char in str(input):
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            count += 1
    return count
    
print(count_vowels('november'))
    
'''
#2. Write a function called is_palindrome(s) that checks whether a string is a
palindrome
(reads the same forward and backward, ignoring case). The function should
returns
either True or False.
'''
def is_palindrome(s):
    pointa = 0
    pointb = len(s) - 1 #minus 1 because str starts at 0
    check = True
    
    while pointa < pointb:
        if s[pointa] != s[pointb]:
            check = False
        pointa += 1
        pointb -= 1
    
    return check
print(is_palindrome('racecars'))
'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
For example, water is very effective to fight fire.
Write a function called type_advantage(attacker, defender) that takes two
Pokémon types as
strings and returns "Super Effective", "Not Very Effective", or "Neutral" based
on
simple type effectiveness rules. Your solution only needs to work for these
three sets of input:
print(type_advantage("Water", "Fire")) # "Super Effective"
print(type_advantage("Fire", "Water")) # "Not Very Effective"
print(type_advantage("Electric", "Grass")) # "Neutral"
'''
def type_advantage(attacker, defender): #I don't know Pokemon hopefully this is right
    effect = ''
    
    if attacker == 'Water':
        if defender == 'Water':
            effect = 'Neutral'
        elif defender == 'Fire':
            effect == 'Super Effective'
        elif defender == 'Grass':
            effect == 'Not Very Effective'
    elif attacker == 'Fire':
        if defender == 'Water':
            effect = 'Not Very Effective'
        elif defender == 'Fire':
            effect == 'Neutral'
        elif defender == 'Grass':
            effect == 'Super Effective'
    elif attacker == 'Grass':
        if defender == 'Water':
            effect = 'Super Effective'
        elif defender == 'Fire':
            effect == 'Not Very Effective'
        elif defender == 'Grass':
            effect == 'Neutral'
    return effect

print(type_advantage('Fire','Water'))
'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
State Ferry fare
based on age and whether the person has a vehicle. Assume the following rates:
* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
* Children (0-18): Free.
'''
def ferry_fare(age, vehicle):
    cost = 0
    if age >= 65:
        cost = 5
        if vehicle == True:
            cost = 15
    elif age >= 19:
        cost = 10
        if vehicle == True:
            cost = 20
    elif age <= 18:
        cost = 0
    return ("Price is $"+str(cost))

print(ferry_fare(78,True))
'''
#5. Write a function called level_up(experience) that takes a player's experience
points
and returns their new level based on these rules:
* 0-99 XP → Level 1
* 100-199 XP → Level 2
* 200+ XP → Level 3
'''
def level_up(exp):
    level = 1
    if exp >= 200:
        level = 3
    elif exp >= 100:
        level = 2
    return ("You are Level "+str(level))

print(level_up(157))
