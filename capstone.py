""" 
Specifications
 1. Create a Person class that is an abstract class that has the following methods
   a. getFullName method
   b. addRequest method
   c. checkRequest method
   d. addUser method
"""
from abc import ABC, abstractclassmethod

class Person(ABC):
    @abstractclassmethod
    def get_full_name(self):
        pass
    @abstractclassmethod
    def add_request(self):
        pass
    @abstractclassmethod
    def check_request(self):
        pass    
    @abstractclassmethod
    def add_user(self):
        pass    



""" 
2. Create an Employee class from Person with the following properties and methods
   a. Properties(make sure they are private and have getters/setters)
       firstName, lastName, email, department

   b. Methods
       Abstract methods
       For the checkRequest and addUser methods, they should do nothing.
       login() - outputs "<Email> has logged in"
       logout() - outputs "<Email> has logged out"
       Note: All methods just return Strings of simple text
           ex. Request has been added
"""

class Employee(Person):
    def __init__(self, first_name, last_name, email, department):
        super().__init__()
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._department = department

# Getters
    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_email(self):
        return self._email

    def get_department(self):
        return self._department

    #setters
    def set_first_name(self):
        self._first_name = first_name

    def set_last_name(self):
        self._last_name = last_name

    def set_email(self):
        self._email = email

    def set_department(self):
        self._department = department


# Methods:
    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"
    def add_request(self):
        return "Request has been added"
    def check_request(self):
        pass    
    def add_user(self):
        pass 

    def login(self):
        return f"{self._email} has logged in"
    def logout(self):
        return f"{self._email} has logged out"

"""
 3. Create a TeamLead class from Person with the following properties and methods
   a. Properties(make sure they are private and have getters/setters)
       firstName, lastName, email, department, members
b. Methods
       Abstract methods
       For the addRequest and addUser methods, they should do nothing.
       login() - outputs "<Email> has logged in"
       logout() - outputs "<Email> has logged out"
       addMember() - adds an employee to the members list
       Note: All methods just return Strings of simple text
          ex. Request has been added
"""

class TeamLead(Person):
    def __init__(self, first_name, last_name, email, department):
        super().__init__()
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._department = department
        self._members = []

    #getters
    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_email(self):
        return self._email

    def get_department(self):
        return self._department

    def get_members(self):
        return self._members

    #setters
    def set_first_name(self):
        self._first_name = first_name

    def set_last_name(self):
        self._last_name = last_name

    def set_email(self):
        self._email = email

    def set_department(self):
        self._department = department

    def set_members(self):
        self._members = members

    #methods
    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"
    def add_request(self):
        pass
    def check_request(self):
        print(f"Request has been checked")    
    def add_user(self):
        pass 

    def login(self):
        print(f"{self._email} has logged in")
    def logout(self):
        print(f"{self._email} has logged out")

    def add_member(self, employee ):
        return self._members.append(employee)


""" 
4. Create an Admin class from Person with the following properties and methods
   a. Properties(make sure they are private and have getters/setters)
      firstName, lastName, email, department

   b. Methods
      Abstract methods
      For the checkRequest and addRequest methods, they should do nothing.
      login() - outputs "<Email> has logged in"
      logout() - outputs "<Email> has logged out"
       addUser() - outputs "New user added"
      Note: All methods just return Strings of simple text
           ex. Request has been added

"""


class Admin(Person):
    def __init__(self, first_name, last_name, email, department):
        super().__init__()
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._department = department

    #getters
    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_email(self):
        return self._email

    def get_department(self):
        return self._department

    #setters
    def set_first_name(self):
        self._first_name = first_name

    def set_last_name(self):
        self._last_name = last_name

    def set_email(self):
        self._email = email

    def set_department(self):
        self._department = department

    #methods
    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"
    def add_request(self):
        pass
    def check_request(self):
        pass
    def add_user(self):
        return "User has been added"  

    def login(self):
        print(f"{self._email} has logged in")
    def logout(self):
        print(f"{self._email} has logged out")

 """
 5. Create a Request that has the following properties and methods
      a. properties
         name, requester, dateRequested, status
      b. Methods
          updateRequest
          closeRequest
         cancelRequest
         Note: All methods just return Strings of simple text
              Ex. Request < name > has been updated/closed/cancelled
"""

class Request():
    def __init__(self, name, requester, date_requested):
        self._name = name
        self._requester = requester
        self._date_requested = date_requested

    #getters
    def get_name(self):
        return self._name

    def get_requester(self):
        return self._requester

    def get_date_requested(self):
        return self._date_requested

    #setters
    def set_name(self):
        self._name = name

    def set_requester(self):
        self._requester = requester

    def set_date_requested(self):
        self._date_requested = date_requested

    def set_status(self, status):
        return {status}

    def update_request(self):
        print(f"Request {self._name} has been updated")  
    def close_request(self):
        return f"Request {self._name} has been closed"
    def cancel_request(self):
        print(f"Request {self._name} has been cancelled") 

# Test cases:
employee1 = Employee("John", "Doe", "djohn@mail.com", "Marketing")
employee2 = Employee("Jane", "Smith", "sjane@mail.com", "Marketing")
employee3 = Employee("Robert", "Patterson", "probert@mail.com", "Sales")
employee4 = Employee("Brandon", "Smith", "sbrandon@mail.com", "Sales")

admin1 = Admin("Monika", "Justin", "jmonika@mail.com", "Marketing")
teamLead1 = TeamLead("Michael", "Specter", "smichael@mail.com", "Sales")
req1 = Request("New hire orientation", teamLead1, "27-Jul-2021")
req2 = Request("Laptop repair", employee1, "1-Jul-2021")

assert employee1.get_full_name() == "John Doe", "Full name should be John Doe"
assert admin1.get_full_name() == "Monika Justin", "Full name should be Monika Justin"
assert teamLead1.get_full_name() == "Michael Specter", "Full name should be Michael Specter"
assert employee2.login() == "sjane@mail.com has logged in"
assert employee2.add_request() == "Request has been added"
assert employee2.logout() == "sjane@mail.com has logged out"

teamLead1.add_member(employee3)
teamLead1.add_member(employee4)
for indiv_emp in teamLead1.get_members():
    print(indiv_emp.get_full_name())

assert admin1.add_user() == "User has been added"

req2.set_status("closed")
print(req2.close_request())
