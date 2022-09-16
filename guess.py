import random


def guess(n: int): # define function to have input int
    guessNum = int(input("Guess a number")) # Ask user for guess
    #print(n) test to see if the function works properly
    while(n != guessNum ): # while the number is incorrect
        if(n < guessNum): # if guess number is greater than actual number
            print("Too High!")
            guessNum = int(input("Guess again!")) # ask for another guess
        elif(n > guessNum): # else if guess number is less than actual number
            print("Too Low!")
            guessNum = int(input("Guess again!")) # ask for another guess
    print("Correct number!")

def main():
    num = random.randint(1, 100) # Get random number
    guess(num) # use guess function with the random number generated
    answer = input("Do you want to play again? Enter y for yes.")
    while answer == "y":
        num2 = random.randint(1, 100) # if the user puts y, continue to generate random number
        guess(num2) # use funciton with new random number
        answer = input("Do you want to play again? Enter y for yes.")

    print("Thank you for playing!") #stops if user doesn't put y


if __name__ == "__main__":
    main()
