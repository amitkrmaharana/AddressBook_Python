class Contacts:

    def __init__(self, contact_dict):
        self.first_name = contact_dict["first_name"]
        self.last_name = contact_dict["last_name"]
        self.address = contact_dict["address"]
        self.city = contact_dict["city"]
        self.state = contact_dict["state"]
        self.zip = contact_dict["zip"]
        self.phone_number = contact_dict["phone_number"]
        self.email = contact_dict["email"]

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_zip(self):
        return self.zip

    def set_zip(self, zip):
        self.zip = zip

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    # magic/dunder method 
    def __str__(self):
        return "First Name = " + self.first_name + \
               " Last Name = " + self.last_name + \
               " Address = " + self.address + \
               " City = " + self.city + \
               " State = " + self.state + \
               " Zip = " + self.zip + \
               " Phone Number = " + self.phone_number + \
               " Email = " + self.email
