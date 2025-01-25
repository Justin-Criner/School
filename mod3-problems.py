# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. 
word1 = input('Give me a word: ')
wordrepeat = int(input('How many times are we repeating that? '))

print(word1*wordrepeat)

#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."

name = input('What is your name? ')
age = int(input('How old are you? '))

print('Hello, '+name+"! You are "+str(age)+" years old. Next year, you will be "+str(age+1)+" years old.")

#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)

sentence = input('Give me a short sentence: ')
word2 = input('Give me a word to find in that sentence: ')

print(word2 in sentence)

#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.

word3 = input('Give me a word to split: ')
indx1 = int(input('Index 1: '))
indx2 = int(input('Index 2: '))

print(word3[indx1:indx2])

#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.

print('Print|three|words') #just kidding

list = ['Print','three','words']
print(list[0], list[1], list[2], sep="|")
