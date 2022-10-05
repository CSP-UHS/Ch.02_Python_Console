# This is my learning about python
# this is another line
import random

# a = 4
# b = 5
# c = 20
# d = 30
# if d == 5:
#     print("You found 5!")
# else:
#     print("The number is not 5")
#
# print("done")

#LOOPING
#range() means how many times the loop repeats
# for i in range(1,11):
#     print(i)

# for i in range(0,101,2):
#     print(i)
#
# for i in range(100, -1, -2):
#     print(i)
#
# total = 0
# for i in range(5):
#     num = int(input("Enter a number: "))
#     total += num
# print("Your total is ", total)

# total = 0
# for i in range(10):
#     total += 1
#     for j in range(10):
#         total += 1
# print(total)

#While not done:
# done = False
# perserverance = 0
# while not done:
#     quit = input("Do you want to quit? (type y)")
#     if quit.lower() == "y":
#         done = True
#     else:
#         perserverance += 1
# print("Goodbye! Your perserverance level is ", perserverance)

# for i in range(10):
#     num = random.randrange(50)
#     print(num)

num = random.randrange(101)
guess = int(input("Guess my number: "))
wrongGuess = 0
playAgain = "y"
while playAgain == "y":
    while guess != num:
        if guess > num:
            wrongGuess += 1
            print("No that's too high")
            guess = int(input("Guess again!"))
        elif guess < num:
            wrongGuess += 1
            print("No that's too low")
            guess = int(input("Guess again!"))
    print("Good job you got it right")
    print("That took you", wrongGuess, "guesses")
    playAgain = input("Would you like to play again? (type y) ")
    if playAgain == "y":
        wrongGuess = 0
        num = random.randrange(101)
        guess = int(input("Guess my number: "))
print("Goodbye!")
