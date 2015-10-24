import random

print ("\t Welcome to 'Guess My Number'!")
print("I'm thinking of a number between 1 and 100.")
number = random.randrange(1,101)
print("Try to guess it in as few attempts and possible.")

user_guess = 0
count = 0

while user_guess != number:
    user_guess = eval(input("Take a guess: "))
    count += 1
    if user_guess < number:
        print("higher...")
    if user_guess > number:
        print("lower...")

print("You guessed it! The number was",number)
print("And it only took you",count,"guesses.")
