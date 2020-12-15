from person import Person
from vehicle import Vehicle

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

sonny.print_phone_email()
jordan.print_phone_email()

car = Vehicle("Nissan", "Leaf", 2015)

car.print_info()
