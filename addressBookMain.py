from address_book import Contacts

contact_dict = {}


class AddressBookMain:

    def __init__(self):
        self.contact_list = []

    def add_contacts(self):
        """

        :return: add a contact list consisting of new contact details
        """
        contact_dict = {
            "first_name": input("Enter your first name: "),
            "last_name": input("Enter your last name: "),
            "address": input("Enter your address: "),
            "city": input("Enter your city name: "),
            "state": input("Enter your state name: "),
            "zip": input("Enter your zip code: "),
            "phone_number": input("Enter your phone number: "),
            "email": input("Enter your email: ")
        }
        contact = Contacts(contact_dict)
        self.contact_list.append(contact)

    def update_contact(self):
        """

        :return: to update a contact
        """
        first_name = input("Enter your first name to edit your contact: ")
        for contacts in self.contact_list:
            if contacts.first_name == first_name:
                self.contact_to_edit(contacts)
                break
            else:
                pass

    def contact_to_edit(self, contacts):
        """

        :param contacts: object from contact_list
        :return: edited contacts as an object
        """
        choice = int(input("Press the corresponding number you want to edit\n" +
                           "1. First Name\n2. Last Name\n3. Address \n4. City\n5. State\n" +
                           "6. Zip\n7. phone number\n8. email\n"))
        if choice == 1:
            contacts.first_name = input("Update First Name: ")
        elif choice == 2:
            contacts.last_name = input("Update Last Name: ")
        elif choice == 3:
            contacts.address = input("Update Address")
        elif choice == 4:
            contacts.city = input("Update City: ")
        elif choice == 5:
            contacts.state = input("Update State")
        elif choice == 6:
            contacts.zip = input("Update Zip")
        elif choice == 7:
            contacts.phone_number = input("Update Phone Number")
        elif choice == 8:
            contacts.email = input("Update Email")
        else:
            print("Invalid Input. TRY AGAIN!!")

    def actions(self):
        """

        :return: traversing the address book to perform specific actions
        """
        check = True
        while check:
            choice = int(input("Press the corresponding number according to your action required:"
                               "\n1. ADD CONTACTS\n2. UPDATE CONTACTS"
                               "\n3. PRINT CONTACTS\n4. DELETE CONTACT\n5. EXIT\n"))
            if choice == 1:
                self.add_contacts()
            elif choice == 2:
                self.update_contact()
            elif choice == 3:
                for contacts in self.contact_list:
                    print(contacts)
            elif choice == 4:
                self.__del__()
            elif choice == 5:
                check = False
            else:
                print("Invalid Input")

    def __del__(self):
        first_name = input("Enter your first name to delete your contact: ")
        for contacts in self.contact_list:
            index = 0
            if contacts.first_name == first_name:
                del self.contact_list[index]
                break
            else:
                pass
            index += 1


address = AddressBookMain()
address.actions()
