import address_book

contact_list = []


class AddressBookMain:
    # Taking contact details from user as input
    @staticmethod
    def create_contacts():
        contact_dict = {
            "first_name": input("Enter your first name:"),
            "last_name": input("Enter your last name:"),
            "address": input("Enter your address:"),
            "city": input("Enter your city name:"),
            "state": input("Enter your state name:"),
            "zip": input("Enter your zip code:"),
            "phone_number": input("Enter your phone number:"),
            "email": input("Enter your email:")
        }
        contact = address_book.Contacts(contact_dict)
        contact_list.append(contact)


AddressBookMain.create_contacts()
for object1 in contact_list:
    print(object1)
