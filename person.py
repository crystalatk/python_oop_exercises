class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1

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
