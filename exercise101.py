# =================== #
# Number 1

# name = input("What is your name? ")
# print("Hello {}, nice to meet you!".format(name))

# =================== #
# Number 2

# name = input("What is your name? ")
# letters = len(name)
# print("Hello, ", name.upper(),"!")
# print("Your name has {} letters in it! Totally cool!".format(letters))

# =================== #
# Number 3

# print("Please fill in the sentence below:")
# print("""
# On your way to the ____(place)____, you encounter a(n) ____(animal)____.
# You get spooked and run into a ____(object)____. Ouch!
# """)
# place1 = input("What is a place?")
# animal1 = input("What is an animal?")
# object1 = input("What is an object?")

# print("""
# On your way to the {place}, you encounter a(n) {animal}.
# You get spooked and run into a {object1}. Ouch!
# """.format(place=place1, animal=animal1, object1=object1))

# =================== #
# Number 4

# day = int(input('Day (0-6)? '))

# if day == 0:
#     print("Sunday")
# elif day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# else:
#     print("Please pick a number between 0 and 6.")

# =================== #
# Number 5

# day = int(input('Day (0-6)? '))

# if day == 1 or day == 6:
#     print("Sleep in!")
# elif day >= 2 and day <= 5:
#     print("Go to Work!")
# else:
#     print("That's not a day of the week!")

# =================== #
# Number 6

# celsius = input("What is the temperature in Celsius? ")
# fahrenheitTemp = int(celsius) * 1.8 + 32
# print("The temperature in Fahrenheit is {}.".format(fahrenheitTemp))

# =================== #
# Number 7

# totalBill = input("What is your total bill amount? ")
# service = input("What was the level of service? (good, fair or bad)")

# if service == "good":
#     tipPerc = .20
# elif service == "fair":
#     tipPerc = .15
# else:
#     tipPerc = .10

# tipAmount = int(totalBill) * tipPerc
# totalAmount = tipAmount + int(totalBill)

# print("Tip amount: ${:.2f}".format(tipAmount))
# print("Total amount: ${:.2f}".format(totalAmount))

# =================== #
# Number 8

# totalBill = input("What is your total bill amount? ")
# service = input("What was the level of service? (good, fair or bad) ")
# split = input("How many people are splitting the check? ")

# if service == "good":
#     tipPerc = .20
# elif service == "fair":
#     tipPerc = .15
# else:
#     tipPerc = .10

# tipAmount = int(totalBill) * tipPerc
# totalAmount = tipAmount + int(totalBill)
# perPersonAmount = totalAmount / int(split)

# print("Tip amount: ${:.2f}".format(tipAmount))
# print("Total amount: ${:.2f}".format(totalAmount))
# print("Amount per person: ${:.2f}".format(perPersonAmount))

# Number 9

# count = 0

# while count < 10:
#     count += 1
#     print(count)

# =================== #
# Number 10

# coins = 0
# while True:
#     print("You have {} coins.".format(coins))
#     more = input("Do you want another? ")
#     another = more.lower()
#     if another == "yes":
#         coins += 1
#     else:
#         print("Bye!")
#         break