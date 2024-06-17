import random
name=input("What is your name?")
print("Welcome",name,"in the hangman game. Good luck !")

words = ['kolkata','ranaghat','python','mango']

word = random.choice(words)

num=0
for x in word:
    num+=1
    print("_", end=" ")
print(" ")
print("Guess the word with",num,"letters.")
guesses = ''


turns = 12

while turns > 0:
    fail = 0
    for char in word:
        if  char in guesses:
            print(char,end=" ")
        else:
            print("_",end=" ")
            fail+=1 
    if fail == 0:
        print("You win")
        print("The word is :", word)
        break

    print()
    guess = input("guess a character :")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong guess! Try again.")
        print("You have",+turns,"more guesses.")


        if turns == 0:
            print("You lost")
            print("\n+---+")
            print(" O  |")
            print("/|\ |")
            print("/ \ |")
            print("   ===") 