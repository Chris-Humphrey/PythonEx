#================================#
## Dictionary Exercises Part 1 ##

# phonebook_dict = { 
#     'Alice': '703-493-1834', 
#     'Bob': '857-384-1234', 
#     'Elizabeth': '484-584-2923'
# }
# # 1
# print(phonebook_dict["Alice"])
# # 2
# phonebook_dict["Kareem"] = "938-489-1234"
# # 3
# del phonebook_dict["Alice"]
# # 4
# phonebook_dict["Bob"] = "968-345-2345"
# # 5
# print(phonebook_dict)


#================================#
## Dictionary Exercises Part 2 ##

# ramit = { 
#     'name': 'Ramit', 
#     'email': 'ramit@gmail.com', 
#     'interests': ['movies', 'tennis'], 
#     'friends': [ 
#         { 
#         'name': 'Jasmine', 
#         'email': 'jasmine@yahoo.com', 
#         'interests': ['photography', 'tennis']
#         }, 
#         { 
#         'name': 'Jan', 
#         'email': 'jan@hotmail.com', 
#         'interests': ['movies', 'tv'] 
#     } 
#     ] 
# }
# 1
# print(ramit["email"])
# 2
# print(ramit["interests"][0])
# 3
# print(ramit["friends"][0]["email"])
# 4
# print(ramit["friends"][1]["interests"][1])


#================================#
## Dictionary Exercises Letter Summary ##

# def letter_histogram(word):
#     myDictionary = {}
#     for letters in word:
#         if myDictionary.get(letters) == None:
#             myDictionary[letters] = 1
#         else:
#             myDictionary[letters] += 1
#     print(myDictionary)

# letter_histogram("banana")



#================================#
## Dictionary Exercises Word Summary ##

# def letter_histogram(word):
#     eachWord = word.lower().split(" ")
#     myDictionary = {}
#     for letters in eachWord:
#         if myDictionary.get(letters) == None:
#             myDictionary[letters] = 1
#         else:
#             myDictionary[letters] += 1
#     print(myDictionary)

# letter_histogram("To be or not to be")
