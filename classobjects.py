# This class is for user bank_account details
class Bank:
    def __init__(self, bank, fname, lname, acc_type, dob, balance, acc_number):
        self.bank = bank
        self.fname = fname
        self.lname = lname
        self.acc_type = acc_type
        self.dob = dob
        self.balance = balance
        self.acc_number = acc_number

# This class captures flight details
class Flight:
    def __init__(self, airline, departure, departure_time, arrival, arrival_time, cost, date):
        self.airline = airline
        self.departure = departure
        self.departure_time = departure_time
        self.arrival = arrival
        self.arrival_time = arrival_time
        self.cost = cost
        self.date = date

# This class be used for planning trips
class Trip:
    def __init__(self, name, destination, date, duration, cost, trip_type):
        self.name = name
        self.destination = destination
        self.date = date
        self.duration = duration
        self.cost = cost
        self.trip_type = trip_type

# In this class we can capture details of someone's favorite football team
class Team:
    def __init__(self, name, country, league, nick_name, create_at, stadium, number_of_players):
        self.name = name
        self.country = country
        self.league = league
        self.nick_name = nick_name
        self.create_at = create_at
        self.stadium = stadium
        self.number_of_players = number_of_players

# This class can be used to capture student details
class Refactory_student:
    def __init__(self, email, fname, lname, programme, dob, start_date, marks):
        self.email = email
        self.fname = fname
        self.lname = lname
        self.programme = programme
        self.dob = dob
        self.start_date = start_date
        self.marks = marks

# In this class we are getting details of an employee
class Employee:
    def __init__(self, email, fname, lname, department, dob, role, salary):
        self.email = email
        self.fname = fname
        self.lname = lname
        self.department = department
        self.dob = dob
        self.role = role
        self.salary = salary

# This class can be used when planning activities one can do on a trip or vacation
class Activity:
    def __init__(self, name, description, location, duration, time, cost, country):
        self.name = name
        self.description = description
        self.location = location
        self.duration = duration
        self.time = time
        self.cost = cost
        self.country = country

# We can use this use this class to record farm details
class Farm:
    def __init__(self, farm_name, manager_name, manager_contact, farm_location, country, farm_type, size):
        self.farm_name = farm_name
        self.manager_name = manager_name
        self.manager_contact = manager_contact
        self.farm_location = farm_location
        self.country = country
        self.farm_type = farm_type
        self.size = size


# This is how we can use the respective classes
person1 = Bank("stabic", "Caleb", "Kanye", "savings", "2 April", 490000000, 234565432365)
person2 = Flight("Emirate", "Entebbe", "11:45", "Paris", "20:15", 1200, "12 Sep")
person3 = Team("Arsenal", "England", "Premier League", "Gunners", 1802, "Emirates", 27)
person4 = Refactory_student("cris@refactory.com", "Chris", "Balyomunsi", "Javascript", "6 Feb", "14 July", 79)
person5 = Employee("bob@bou.ug", "Bob", "Jacob", "IT", "28 Sept", "Head of Software", 28000000)
person6 = Farm("Bulambuli farm", "Ossay", "+256612765456", "Mbale", "Uganda", "Livestock", 13.6)

# This how we can print data from the respective classes
print(person2.cost)

