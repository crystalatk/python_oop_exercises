class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def print_phone_email(self):
        print(f'''
Here is {self.name}'s contact info:
Phone number: {self.phone}
Email Address: {self.email}
''')
