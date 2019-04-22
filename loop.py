#======================#
## Loop Exercises Part 1

# for num in range(1,11):
#     print(num)


#======================#
## Loop Exercises Part 2

# for num in range(int(input("Start on what number?")), int(input("End on what number?"))+1):
#     print(num)

#======================#
## Loop Exercises Part 3

# for num in range(1,10,2):
#     print(num)


#======================#
## Loop Exercises Part 4

# char = ("*****")
# n = 5

# while n > 0:
#     print(char)
#     n -= 1



#======================#
# Loop Exercises Part 5
# char = "*"
# n = int(input("How big is the square?"))
# s = n

# while n > 0:
#     print(char * s)
#     n -= 1


#======================#
# Loop Exercises Part 6
## First and last = w

# char = "*"
# w = int(input("What is the width?"))
# h = int(input("What is the height?"))
# first = w
# last = h

# while last > -1:
#     if(last == h) or (last == 0):
#         print(char * w)
#         last -= 2
#     else:
#         print(char + (" " * (w - 2)) + char)
#         last -= 1


#======================#
# Loop Exercises Part 7
# unfinished

# char = "*"
# num = 7
# nums = num
# space = " "

# while num == 7:
#     if(nums == num):
#         print((space * (num / 2 - .5)) + char + (space * (num / 2 - .5)))

# print((space * (num / 2 - .5)) + char + (space * (num / 2 - .5)))


#======================#
# Loop Exercises Part 9

# for num in range(1,11):
#     for inner in range(1,11):
#         result = num * inner
#         print(num, "*" , inner , "=" , result)


#======================#
# Loop Exercises BONUS - print a banner

# text = input("What would you like to say?")
# length = len(text)
# char = "*"

# while True:
#     print(char * (length + 4))
#     print(char + " " + text + " " + char)
#     print(char * (length + 4))
#     break