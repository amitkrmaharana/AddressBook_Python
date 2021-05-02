import csv

from address_book import Contacts

contact_dict = {}


class AddressBookMain:

    def __init__(self):
        self.contact_book = {}

    def write_to_csv_file(self):
        with open('Contact_Details.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            for key, value in self.contact_book.items():
                csv_writer.writerow(key)
                for contacts in value:
                    contact = contacts.__dict__
                    csv_writer.writerow(contact.values())

    def add_contacts(self, contact_name, contact_list):
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
        contact_list.append(contact)
        self.contact_book[contact_name] = contact_list

    def update_contact(self, contact_list):
        """

        :return: to update a contact
        """
        first_name = input("Enter your first name to edit your contact: ")
        for contacts in contact_list:
            if contacts.first_name == first_name:
                self.contact_to_edit(contacts)
                break
        else:
            print(f"{first_name} does not exist")

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

    def remove_contact(self, contact_list):
        """

        :return: deleted a selected contact by it's First Name
        """
        name = input("Enter your first name to delete your contact: ")
        index = 0
        for contacts in contact_list:
            if contacts.first_name == name:
                del contact_list[index]
                break
            index += 1
        else:
            print(f"{name} not in contact book")

    def contact_list_action(self, contact_name, contact_list):
        """

        :return: traversing the contact list to perform specific actions
        """
        check = True
        while check:
            choice = int(input("Press the corresponding number according to your action required:"
                               "\n1. ADD CONTACTS\n2. UPDATE CONTACTS"
                               "\n3. PRINT CONTACTS\n4. DELETE CONTACT\n5. SORT BY FIRST NAME\n6. EXIT\n"))
            if choice == 1:
                self.add_contacts(contact_name, contact_list)
            elif choice == 2:
                self.update_contact(contact_list)
            elif choice == 3:
                for contacts in contact_list:
                    print(contacts)
            elif choice == 4:
                self.remove_contact(contact_list)
            elif choice == 5:
                contact_list = self.sort_by_first_name(contact_list)
            elif choice == 6:
                check = False
            else:
                print("Invalid Input")

    def address_book_action(self):
        """

        :return: traversing the address book to perform specific actions
        """

        check_bool = True
        while check_bool:
            choice = int(input("Press the corresponding number according to your action required: "
                               "\n1. NEW ADDRESS BOOK\n2. EXISTING ADDRESS BOOK\n3. WRITE TO CSV FILE\n4.EXIT\n"))
            if choice == 1:
                self.add_new_address_book()
            elif choice == 2:
                name = input("Enter the name of your address book: ")
                for contact_name in self.contact_book:
                    if contact_name == name:
                        self.contact_list_action(contact_name, self.contact_book[contact_name])
                else:
                    print(f"{name} does not exist")
            elif choice == 3:
                self.write_to_csv_file()
            elif choice == 4:
                check_bool = False
            else:
                print("Invalid Input. TRY AGAIN!!")

    def add_new_address_book(self):
        """

        :return: adding a new address book
        """
        contact_list = []
        name = self.unique_name_check()
        self.add_contacts(name, contact_list)
        self.contact_list_action(name, self.contact_book[name])

    def unique_name_check(self):
        """

        :return: checking if the name is unique or not
        """
        check = True
        while check:
            name = input("Enter a unique name for your address book: ")
            for contact_name in self.contact_book:
                if contact_name == name:
                    print("Try Again!! Name already exist")
                    break
            else:
                check = False
        return name

    def sort_by_first_name(self, contact_list):
        return sorted(contact_list, key=lambda contact: contact.first_name)


address = AddressBookMain()
address.address_book_action()
