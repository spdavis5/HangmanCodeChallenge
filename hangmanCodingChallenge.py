#Spencer Davis
#Hangman Coding Challenge
#11/9/2024

#Import random package
import random

def play_game():
    #Greet the user to the game
    print("Welcome to the game!")
    print("Try and guess the random word.")

    #Generate list of 10 random words
    wordsList = ["coding","cougars","programming","lambda","terminal","microsoft","debugging","loop","remote","software"]

    #Choose a random word for the user
    userWord = random.choice(wordsList)

    #Tell the user how many characters are in the word they are given
    print(f"Your word is {len(userWord)} characters long.")

    #Generate a list that is made up of their guesses. For empty places, put a _
    wordGuess = ["_" for letter in userWord]

    #Keep a count of user guess count, with correct and incorrect guesses, plus letters they have already guessed
    guessCount = 0
    correctGuesses = 0
    incorrectGuesses = 0
    guessBox = []

    #Make running variable for input while loop
    running = True
    #Start loop to continually gather user guesses
    while running:
        #Show the hangman word as a string instead of a list. Concatinate each character of list to a new string called output
        output = ""
        #For every character in their guessed word
        for x in wordGuess:
            #Add character to output string
            output += x
        #Display output, and words guessed with correct and incorrect guesses
        print(output)
        print(f"Words guessed: {guessBox}")
        print(f"Correct Guesses: {correctGuesses}")
        print(f"Incorrect Guesses: {incorrectGuesses}")

        #Get guess from user
        userGuess = input("Letter Guess: ").lower()

        #Validate input
        #Character is only one letter
        if len(userGuess) != 1:
            print("Please enter a single letter.")
            continue
        #They haven't guessed that letter before
        if userGuess in guessBox:
            print("You've already guessed that letter. Please try again.")
            continue

        #Add guess to the box of already guessed letters
        guessBox.append(userGuess)
        #Increment guess count
        guessCount += 1
        #Keep track of how many letters they get correct
        lettersCorrect = 0

        #Keep count of what character we are on
        charCount = 0
        #Flag to check if the guess was correct
        guessCorrect = False
        #Loop through each character in the word
        for char in userWord:
            #Increment character count
            charCount += 1
            #If the user guess is the same as a character
            if char == userGuess:
                wordGuess[charCount-1] = userGuess
                guessCorrect = True

        #Update correct or incorrect guesses
        if guessCorrect:
            correctGuesses += 1
        else:
            incorrectGuesses += 1

        #Check if game is finished by looping through word guess and check if there is still a _.
        for letter in wordGuess:
            #Keep going if there is a _
            if letter == "_":
                continue
            #If the letter isn't a _, add one to the correct count
            else:
                lettersCorrect += 1
        #If the number of correct letters is equal to the length of the word, the user has won
        if lettersCorrect == len(userWord):
            print(f"You have guessed the correct word {userWord}")
            print(f"It took you {guessCount} guesses.")
            running = False

def main():
    play_again = True
    while play_again:
        play_game()
        response = input("Do you want to play again? (y/n): ").lower()
        if response != 'y':
            play_again = False
            print("Thanks for playing!")

if __name__ == "__main__":
    main()
