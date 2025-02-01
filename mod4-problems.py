#1. Construct a truth table for the expression: (A AND B) OR (NOT B) where A and B each can be True or False. Your truth table should be commented out (as it's not valid Python code!)
'''
A       B       A AND B
--------------------------
True    True    True
True    False   False
False   True    False
False   False   False

B       NOT B
---------------
True    False
False   True

'''
#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".

sensor = int(input('What is the sensor reading?'))
if sensor < 8:
    print('Headlights On')
else:
    print('Headlights Off')

#3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100. Print True if the user’s balance is below $100; print False, otherwise.

balance = float(input('How many dollars are in your bank account?: $'))
print(balance < 100)

#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.

age = int(input('How old are you?: '))
if age >= 18:
    print('You can see any movie rating.')
elif age >= 13:
    print('You can see up to PG-13 rated movies.')
else:
    print('You can see G rated movies.')
    
#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. Ask the user for the order total and print the total cost, including shipping.

order = float(input('How much is your order total?: $'))
if order >= 50:
    print(f'Your total is: ${order:.2f}')
else:
    print(f'Your total is: ${order + 5:.2f}')
