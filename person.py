class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.num_unique_people_greeted = 0
        self.people_greeted = []

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        new_person = True
        for each in self.people_greeted:
            if other_person.name == each:
                new_person = False
        if new_person:
            self.people_greeted.append(other_person.name)
            self.num_unique_people_greeted += 1

    def print_contact_info(self):
        print(f'''
Here is {self.name}'s contact info:

{self.name}'s email: {self.email}
{self.name}'s phone number: {self.phone}
''')

    def add_friends(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        print(len(self.friends))

    def __str__(self):
        return f'''
This is a Person! 
    Name: {self.name} 
    Email: {self.email} 
    Phone #: {self.phone}
'''
