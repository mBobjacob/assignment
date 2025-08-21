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
bank_accounts1 = Bank("stabic", "Caleb", "Kanye", "savings", "2 April", 490000000, 234432876365)
bank_accounts2 = Bank("DFCU", "Esther", "Bate", "salary", "2 Mar", 44000000, 234565488665)
bank_accounts3 = Bank("ECO bank", "Charlotte", "Bukenya", "savings", "23 Nov", 90000000, 754565432365)
bank_accounts4 = Bank("Centinary", "Leon", "Barigye", "salary", "30 Jun", 4900000, 23456523365)
bank_accounts5 = Bank("stabic", "Fiona", "Gashom", "savings", "29 Oct", 94000000, 234565342366)
bank_accounts6 = Bank("Diamond trust bank", "Museveni", "Tubuhaburwa", "salary", "22 May", 4000000, 2345643232365)

flights1 = Flight("Emirate", "Entebbe", "11:45", "Paris", "20:15", 1200, "12 Sep")
flights2 = Flight("Ethihad", "London", "121:45", "Prague", "23:25", 1200, "12 Sep")
flights3 = Flight("Fly Dubai", "Dubai", "15:55", "London", "22:35", 1200, "12 Sep")
flights4 = Flight("Kenya Airways", "Paris", "13:45", "Nairobi", "14:40", 1200, "12 Sep")
flights5 = Flight("Fly Dubai", "Dubai", "09:15", "Kampala", "16:15", 1200, "12 Sep")
flights6 = Flight("Qatar", "Prague", "12:45", "Dubai", "4:15", 1200, "12 Sep")

football_teams1 = Team("Arsenal", "England", "Premier League", "Gunners", 1802, "Emirates", 27)
football_teams2 = Team("Chelsea", "England", "Premier League", "blues", 1843, "Stanford Bridge", 45)
football_teams3 = Team("Man United", "England", "Premier League", "Red devils", 1800, "Old traford", 30)
football_teams4 = Team("Nottingham Forest", "England", "Premier League", "Forest", 1834, "City stadium", 20)
football_teams5 = Team("Man City", "England", "Premier League", "Noisy neighbours", 1822, "Ethihad", 25)
football_team6 = Team("KCCA Fc", "Uganda", "Uganda Premier League", "Kasasilo boys", 1989, "KCCA grounds", 23)

students1 = Refactory_student("cris@refactory.com", "Chris", "Balyomunsi", "Javascript", "19 Aug", "14 Feb", 75)
students2 = Refactory_student("martha@refactory.com", "Martha", "Kanyike", "Cyber", "6 Feb", "14 July", 80)
students3 = Refactory_student("Precious@refactory.com", "Precious", "Namara", "Python", "28 Feb", "1 Jun", 32)
students4 = Refactory_student("Opio@refactory.com", "Opio", "Derick", "Javascript", "6 Jun", "14 July", 89)
students5 = Refactory_student("benon@refactory.com", "Benon", "Mwinginya", "Data Analysis", "21 Nov", "14 July", 79)
students6 = Refactory_student("faith@refactory.com", "faith", "Mutoni", "Javascript", "3 Jan", "14 Feb", 59)

employees1 = Employee("bob@bou.ug", "Bob", "Jacob", "IT", "28 Sept", "Head of Software", 28000000)
employees2 = Employee("Ivan@bou.ug", "Ivan", "Bukenya", "Procurement", "28 Mar", "Head of Procurement", 15000000)
employees3 = Employee("isaac@bou.ug", "Isaac", "Ninja", "Operations", "15 Dec", "Transport", 11000000)
employees4 = Employee("carl@bou.ug", "Ayesiga", "Carl", "IT", "30 April", "Software developer", 8000000)
employees5 = Employee("li@bou.ug", "Elizabeth", "Nkuru", "Finance", "13 Oct", "Head of P&L", 26000000)
employees6 = Employee("rober@bou.ug", "Jacob", "Robert", "IT", "7 Nov", "CTO", 58000000)

farm1 = Farm("Bulambuli ", "Ossay", "+256612765456", "Mbale", "Uganda", "Livestock", 13.6)
farm2 = Farm("Bugema ", "Newman", "+25664565456", "Gayaza", "Uganda", "Plantation", 3.9)
farm3 = Farm("Happy plants", "Chris", "+271612765456", "Kinsasha", "Congo", "Fruits", 163.7)
farm4 = Farm("Old mcdonald", "Harrison", "+254612765456", "Kisumu", "Kenya", "Livestock", 1.4)
farm5 = Farm("Buli little birds", "Richard", "+250612765456", "Kigali", "Rwanda", "Poutry", 16)
farm6 = Farm("Soko farm", "Fabian", "+255612765456", "Mwanza", "Tanzania", "Plantaion", 23.1)

# This how we can print data from the respective classes
print(bank_accounts2.acc_type)

