class Bank:
    def __init__(self, bank, fname, lname, acc_type, dob, balance, acc_number):
        self.bank = bank
        self.fname = fname
        self.lname = lname
        self.acc_type = acc_type
        self.dob = dob
        self.balance = balance
        self.acc_number = acc_number

class Flight:
    def __init__(self, airline, departure, departure_time, arrival, arrival_time, cost, date):
        self.airline = airline
        self.departure = departure
        self.departure_time = departure_time
        self.arrival = arrival
        self.arrival_time = arrival_time
        self.cost = cost
        self.date = date

class Trip:
    def __init__(self, name, destination, date, duration, cost, trip_type):
        self.name = name
        self.destination = destination
        self.date = date
        self.duration = duration
        self.cost = cost
        self.trip_type = trip_type

class Team:
    def __init__(self, name, country, league, nick_name, create_at, stadium, number_of_players):
        self.name = name
        self.country = country
        self.league = league
        self.nick_name = nick_name
        self.create_at = create_at
        self.stadium = stadium
        self.number_of_players = number_of_players

class Refactory_student:
    def __init__(self, email, fname, lname, programme, dob, start_date, marks):
        self.email = email
        self.fname = fname
        self.lname = lname
        self.programme = programme
        self.dob = dob
        self.start_date = start_date
        self.marks = marks

class Employee:
    def __init__(self, email, fname, lname, department, dob, role, salary):
        self.email = email
        self.fname = fname
        self.lname = lname
        self.department = department
        self.dob = dob
        self.role = role
        self.salary = salary

class Activity:
    def __init__(self, name, description, location, duration, time, cost, country):
        self.name = name
        self.description = description
        self.location = location
        self.duration = duration
        self.time = time
        self.cost = cost
        self.country = country

class Farm:
    def __init__(self, farm_name, manager_name, manager_contact, farm_location, country, farm_type, size):
        self.farm_name = farm_name
        self.manager_name = manager_name
        self.manager_contact = manager_contact
        self.farm_location = farm_location
        self.country = country
        self.farm_type = farm_type
        self.size = size


person1 = Bank("stabic", "Caleb", "Kanye", "savings", "2 April", 490000000, 234565432365)
person2 = Flight("Emirate", "Entebbe", "11:45", "Paris", "20:15", 1200, "12 Sep")
person3 = Team("Arsenal", "England", "Premier League", "Gunners", 1802, "Emirates", 27)
person4 = Refactory_student("cris@refactory.com", "Chris", "Balyomunsi", "Javascript", "6 Feb", "14 July", 79)
person5 = Employee("bob@bou.ug", "Bob", "Jacob", "IT", "28 Sept", "Head of Software", 28000000)
person6 = Farm("Bulambuli farm", "Ossay", "+256612765456", "Mbale", "Uganda", "Livestock", 13.6)

print(person2.cost)

