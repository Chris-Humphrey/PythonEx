## Guessing Game Part 1

# secret_number = 5
# numGuess = int(input("I am thinking of a number between 1 and 10. What's the number? "))

# while numGuess != secret_number:
#     print("Nope, please try again.")
#     numGuess = int(input("What's the number? "))

# print("Yes! You win!")

#======================#
## Guessing Game Part 2

# secret_number = 5
# numGuess = int(input("I am thinking of a number between 1 and 10. What's the number?"))

# while numGuess != secret_number:
#     if numGuess > secret_number:
#         numGuess = int(input(f"{numGuess} is too high. What's the number? "))
#     elif numGuess < secret_number:
#         numGuess = int(input(f"{numGuess} is too low. What's the number?"))

# print("Yes! You win!")

#======================#
## Guessing Game Part 3

# import random
# secret_number = random.randint(1,10)

# numGuess = int(input("I am thinking of a number between 1 and 10. What's the number?"))

# while numGuess != secret_number:
#     if numGuess > secret_number:
#         numGuess = int(input(f"{numGuess} is too high. What's the number? "))
#     elif numGuess < secret_number:
#         numGuess = int(input(f"{numGuess} is too low. What's the number?"))

# print("Yes! You win!")

#======================#
## Guessing Game Part 4

# import random
# secret_number = random.randint(1,10)

# limGuess = 5
# numGuess = int(input(f"I am thinking of a number between 1 and 10. You have {limGuess} guesses left. What's the number?"))

# while numGuess != secret_number and limGuess >= 0:
#     limGuess -= 1
#     if numGuess > secret_number and limGuess > 0:
#         numGuess = int(input(f"{numGuess} is too high. You have {limGuess} guesses left. What's the number? "))
#     elif numGuess > secret_number and limGuess == 0:
#         print(f"{numGuess} is too high. You ran out of guesses!")
#     elif numGuess < secret_number and limGuess > 0:
#         numGuess = int(input(f"{numGuess} is too low. You have {limGuess} guesses left. What's the number?"))
#     elif numGuess < secret_number and limGuess == 0:
#         print(f"{numGuess} is too low. You ran out of guesses!")

# if numGuess == secret_number:
#     print("Yes! You win!")

#======================#
## Guessing Game Bonus

# def myFunction():
#     import random
#     secret_number = random.randint(1,10)
#     replay = ""
#     limGuess = 5
#     numGuess = int(input(f"I am thinking of a number between 1 and 10. You have {limGuess} guesses left. What's the number?"))

#     while numGuess != secret_number and limGuess >= 0:
#         limGuess -= 1
#         if numGuess > secret_number and limGuess > 0:
#             numGuess = int(input(f"{numGuess} is too high. You have {limGuess} guesses left. What's the number? "))
#         elif numGuess > secret_number and limGuess == 0:
#             replay = input(f"{numGuess} is too high. You ran out of guesses! Do you want to try again? (Y or N)")
#         elif numGuess < secret_number and limGuess > 0:
#             numGuess = int(input(f"{numGuess} is too low. You have {limGuess} guesses left. What's the number?"))
#         elif numGuess < secret_number and limGuess == 0:
#             replay = input(f"{numGuess} is too low. You ran out of guesses! Do you want to try again? (Y or N)")

#     if numGuess == secret_number:
#         replay = input("Yes! You win! Do you want to play again? (Y or N)")

#     if replay == "Y":
#         myFunction()
#     else:
#         print("Game Over. Goodbye!")

# myFunction()