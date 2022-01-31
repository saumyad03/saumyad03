#Hangman Program Using Dictionary
import random

def playHangman():
    infile = open("words.txt", "r")
    words = infile.readlines()
    word = words[random.randint(0, len(words) - 1)]
    unsolvedList = []
    solvedList = []
    solvedDict = {}
    guessedLetters = []

    for c in word:
        solvedList.append(c)
        unsolvedList.append("_")

    for c in solvedList:
        solvedDict[c] = []

    for i in range(len(solvedList)):
        solvedDict[solvedList[i]].append(i)


    guesses = 6

    print("Type in quit to end the game")
    while True:
        for c in unsolvedList:
            print(c, end = ' ')
        guess = input("Guess a letter: ")
        if guess == "quit":
            print("You ended the game")
            break
        while len(guess) != 1 or guess.isalpha() == False:
            print("Invalid guess")
            guess = input("Guess a letter: ")
        if guess in guessedLetters:
            print("You already guessed this letter")
        elif guess in solvedDict:
            guessedLetters.append(guess)
            for letterPosition in solvedDict[guess]:
                unsolvedList.pop(letterPosition)
                unsolvedList.insert(letterPosition, guess)
            if "_" not in unsolvedList:
                for c in unsolvedList:
                    print(c, end = ' ')
                print("You won")
                print("The correct word was ", word)
                break
        else:
            guessedLetters.append(guess)
            guesses -= 1
            if guesses <= 0:
                print("You lost")
                print("The correct word was ", word)
                break
            print(guess, " is not in the word")
            print(guesses, " guesses left")

playHangman()
