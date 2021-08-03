import random

def guess(num):
    newGuess = int(input('Your guess: '))
    if newGuess == num:
        return False
    if newGuess > num:
        print("That number is too high.")
        return True
    elif newGuess < num:
        print("That number is too low.")
        return True
    return True

def main():
    name = input("Hello, please enter your name: ")
    
    number = random.randint(1,100)
    guesses = 0
    guessing = True

    print("I am thinking of a number between 1 and 100, try guessing")

    while guessing:
        guesses += 1
        guessing = guess(number)
    
    print(name, 'won in', guesses, 'turns.')

main()