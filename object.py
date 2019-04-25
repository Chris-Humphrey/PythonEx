"""
PYTHON OBJECT EXERCISE
"""
#======================#
## PERSON CLASS ##
#======================#

class Person: 
    def __init__(self, name, email, phone):
        self.name = name 
        self.email = email 
        self.phone = phone
        self.friends =[]
        self.greeting_count = 0

    def greet(self, other_person):
        self.greeting_count += 1
        return ('Hello {}, I am {}!'.format(other_person.name, self.name))

    def info(self):
        return (f'name: {self.name} | email: {self.email} | phone: {self.phone}')

    def print_contact_info(self):
        return (f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}'")
    
    def add_friend(self):
        friends.append(self)

    def num_friends(self):
        print(f"{self.name} has {len(self.friends)} friend(s)")
    
    def __str__(self): 
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

jordan.friends.append(sonny) 
sonny.friends.append(jordan)
jordan.num_friends()

print(jordan)

# print(sonny.greet(jordan))
# print(sonny.greet(jordan))
# print(jordan.greet(sonny))

people =[sonny, jordan]

# print(sonny.greeting_count)

# for personObject in people:
#     print(personObject.info())

# print(sonny.print_contact_info())

#======================#
## VEHICLE CLASS ##
#======================#

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def print_info(self):
#         return (f"{self.year} {self.make} {self.model}")


# car = Vehicle("Nissan", "Leaf", 2015)
# print(car.make, car.model, car.year)
# print(car.print_info())