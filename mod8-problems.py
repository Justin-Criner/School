'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
'''

with open("gardening_tips.txt", "r") as file_g:
    for line in file_g:
        print(line, end="")

'''
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''

file = open("hiking_log.txt", "w")
user_input = ""
miles = ""
while user_input != "0":
    user_input = input("Name of hike? (Input 0 to stop)")
    if user_input != "0":
        miles = input("How many miles did you hike?")
        file.write(user_input + ", hiked " + miles + " miles\n")
file.close()

file = open("hiking_log.txt", "r")
print(file.read())
file.close()

'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
'''

with open("song_lyrics.txt", "r") as lyrics:

    def word_match(input):
        count = 0
        for line in lyrics:
            for word in line.split():
                if word == input:
                    count += 1
        return count
    
    i1, i2, i3, i4, i5 = input("Give 5 words separated by a space: ").split(" ")
    
    lyric_count = {
        i1: word_match(i1),
        i2: word_match(i2),
        i3: word_match(i3),
        i4: word_match(i4),
        i5: word_match(i5),
    }
    #I cannot figure out why my define wont work after the first iteration?
    print(lyric_count)


'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
'''

with open("poll.txt", "r") as poll:
    
    county = 0
    countn = 0
    
    for line in poll:
        for word in line.split(','):
            if word == "yea":
                county += 1
            elif word == "nay":
                countn += 1
    
    print("Yea: ",county," | Nay: ",countn)
    
    
