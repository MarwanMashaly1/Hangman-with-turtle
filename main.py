"""
Marwan Mashaly
Dec 8, 2020
Assignment 9.2 Hangman with turtle
"""
#-------------------Imports-------------------------------
import random           # imports the random module
import turtle           # allows to use the turtle library
#------------------Turtle setup---------------------------
wn = turtle.Screen()                   # Create a graphics window
wn.bgcolor("light grey")               # set the background color
wn.window_width()
wn.window_height()
tia = turtle.Turtle()                  # tia
tia.pensize(6)
tia.speed(0)                           # set tia speed to 0
tess = turtle.Turtle()                  # tia
tia.speed(0)                           # set tia speed to 0
#-------------------Functions------------------------------
def getWord(line):                 # function to get word
    word = random.choice(line)      # choose random word from file
    return word                     # return chosen word

def play(word):                     # function to play
    wordLen = "_" * len(word)       # get length of word
    guessed = False                 # gussed is false
    lstGuessedLetters = []          # lst of letters guessed
    lstGuessedWords = []            # lst of guessed words
    intTries = 6                    # num of tries
    print("Let's play Hangman")     # print
    print(displayHangman(intTries)) # print
    print(wordLen)                  # print
    tess.pu()                       # pen up
    tess.goto(0,-100)               # 0, -100
    tess.pd()                       # pen down
    tess.write("_ " * len(word) , font=("Arial", 20))   # write on screen
    print("\n")                     # print
    while not guessed and intTries > 0:     # loop until tries finish or win
        strGuess = input("guess a letter or word: ")    # get guess
        if len(strGuess) == 1 and strGuess.isalpha():   # condition if the length of input = 1 and is a letter
            if strGuess in lstGuessedLetters:           # check if it's in list
                print("you already tried ", strGuess)   # print
            elif strGuess not in word:                  # condition if not in word
                print(strGuess, "isn't in the word ")   # print
                intTries -= 1                           # decrease tries
                lstGuessedLetters.append(strGuess)      # add to guessed
            else:                                       # else
                print("Good Job ", strGuess, " is in the word") # print
                lstGuessedLetters.append(strGuess)  # add to list
                lstWord = list(wordLen)             # creates list
                indices = [i for i, letter in enumerate(word) if letter == strGuess]         # seperate word to letters
                for index in indices:       # range to each letter
                    lstWord[index] = strGuess   # give each letter a position in list
                    if index == 0:          # if 1st letter
                        length = len(word) - 1  # decrease length
                        tess.pu()           # pen up
                        tess.write(strGuess + "_ " * length, font=("Arial", 20))    # write on screen
                    elif index == 1:       # if 2nd letter 
                        length = len(word) - 2  # decrease length
                        tess.pu()           # pen up
                        tess.write("_ " + strGuess + "_ " * length, font=("Arial", 20)) # write on screen
                    elif index == 2:        # if 3rd letter
                        length = len(word) - 3  # decrease length
                        tess.pu()           # pen up
                        tess.write("_ " *2+ strGuess + "_ " * length, font=("Arial", 20))   # write on screen
                    elif index == 3:        # if 4th letter
                        length = len(word) - 4  # decrease letter
                        tess.pu()           # pen up
                        tess.write("_ "*3 + strGuess + "_ " * length, font=("Arial", 20))   # write on screen
                    elif index == 4:        # if 5th letter
                        length = len(word) - 5  # decrease length
                        tess.pu()           # pen up
                        tess.write("_ "*4 + strGuess + "_ " * length, font=("Arial", 20))   # write on screen
                    elif index == 5:        # if 6th letter
                        length = len(word) - 6  # decrease length
                        tess.pu()           # pen up
                        tess.write("_ "*5 + strGuess + "_ " * length, font=("Arial", 20))   # write on screen
                    elif index == 6:        # if 7th letter
                        length = len(word) - 7  # decrease length
                        tess.pu()           # pen up
                        tess.write("_ "*6 + strGuess + "_ " * length, font=("Arial", 20))   # write on screen
                    elif index == 7:        # if 8th letter
                        length = len(word) - 8  # decrease length
                        tess.pu()           # pen up
                        tess.write("_ "*7 + strGuess + "_ " * length, font=("Arial", 20))   # write on screen
                wordLen = "".join(lstWord)      # make it a full word again
                if "_" not in wordLen:          # condition if changed to letter
                    guessed = True              # guessed is true
        elif len(strGuess) == len(word) or  len(strGuess) >= len(word)or len(strGuess) <= len(word) and strGuess.isalpha(): # condition if length of guess = word length
            if strGuess in lstGuessedWords:     # condition if it's in list
                print("You already tried ", strGuess)   # print
            elif strGuess != word:                      # if not equal word
                print(strGuess, " is not the word")     # print
                intTries -= 1                         # decrease tries
                lstGuessedWords.append(strGuess)        # add to list
            else:                                       # else
                tess.clear()                            # clear
                tess.write(word, font=("Arial", 20))
                guessed = True                          # guess = true
                wordLen = word                          # length = word
        else:                                           # else
            print("invalid input")                      # print
        print(displayHangman(intTries))                 # print
        print(wordLen)                                  # print
        print("\n")
    if guessed:                                         # if true
        print("Good Job, you guessed the word")         # print
    else:                                               # else
        print("you ran out of tries. The word was " + word + " maybe next time you will get it")                     # print

def displayHangman(intTries):           # function to draw hangman
    if intTries == 0:                   # if tries left 0

        tia.pu()                # pen up
        tia.goto(87.5, 55)      # 87.5
        tia.setheading(225)     # set head
        tia.pd()                # pen down
        tia.fd(30)              # forward
    if intTries == 1:           # if tries left 1
        # hands
        tia.pu()                # pen up
        tia.goto(87.5,55)      # 87.5, 50
        tia.pd()                # pen down
        tia.fd(30)              # forward
    if intTries == 2:           # if tries left 2
        # legs 
        tia.pu()                # pen up
        tia.goto(87.5, 10)      # 87.5
        tia.setheading(315)     # set head
        tia.pd()                # pen down
        tia.fd(25)              # forward
    if intTries == 3:           # if tries left 3
        # legs 
        tia.goto(87.5, 10)      # 87.5
        tia.setheading(215)     # 
        tia.fd(25)              # forward
    if intTries == 4:           # if tries left 4
        
        #body
        tia.pu()                # pen up
        tia.goto(87.5,60)      # 87.5, 70
        tia.pd()                # pen down
        tia.fd(50)              # forward
    if intTries == 5:           # if tries left 5
        #face
        tia.pu()                # pen up
        tia.goto(79,70)         # 80, 80
        tia.pd()                # pen down
        tia.circle(10)          # draw circle
        tia.pu()                # pen up
    if intTries == 6:           # if tries left 6
        tia.pu()                # pen up
        tia.home()              # go home
        tia.setheading(90)      # set head up
        tia.pd()                # pen down
        tia.setheading(90)      # set head up
        tia.pu()                # pen up
        tia.goto(12.5, 10)      # 12.5, 10
        tia.pd()                # pen down
        tia.fd(100)             # forward
        tia.rt(90)              # turn right
        tia.fd(75)              # forward
        tia.rt(90)              # turn right
        tia.fd(30)              # forward
    stages = [0, 1, 2, 3, 4, 5, 6]  # list for lives
    return stages[intTries]         # return

#--------------------Main--------------------------------

file = open("words.txt" , 'r')      # open file to read
line = file.read().splitlines()     # read lines and split them
word = getWord(line)               # call function
play(word)                          # call function
while True:                         # while true
    strGame = input("Would you like to play again (yes/no): ")  # ask user to play again
    if strGame == "no":                     # condition if no
        print("Thank you for playing")      # print
    if strGame == "yes":                 # condition if yes
        tess.clear()                        # clear screen
        tia.clear()                         # clear screen
        word = getWord(line)               # call function to get word
        play(word)                          # call function 
file.close                              # close file