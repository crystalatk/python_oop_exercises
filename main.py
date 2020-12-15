from person import Person
from vehicle import Vehicle

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

sonny.print_contact_info()
jordan.print_contact_info()

car = Vehicle("Nissan", "Leaf", 2015)
truck = Vehicle("Ford", "F-150", 2002)
sport = Vehicle("Audi", "R8", 2021)

car.print_info()
