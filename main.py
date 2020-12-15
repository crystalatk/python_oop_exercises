from person import Person

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

print(f'''
Here is {sonny.name}'s contact info:
Phone number: {sonny.phone}
Email Address: {sonny.email}
''')

print(f'''
Here is {jordan.name}'s contact info:
Phone number: {jordan.phone}
Email Address: {jordan.email}
''')
