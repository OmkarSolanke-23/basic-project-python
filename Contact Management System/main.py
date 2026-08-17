
contact = {}

while True:

    print("======\nContact Management System=====")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. search Contact")
    print("4. Delete Contact")
    print("5. Exit ")

    choice  = input(" Enter The Choice : ")

    # Add Contact 
    if choice == "1":

       name = input("Enter  Name ; ")
       phone = input("Enter  Number : ")

       contact[name] = phone

       print("Contact add Successfully!")

    # view Contact
    elif choice == "2":

        if len(contact) == 0:
            print("contact no found")

        else :
            print("\n----- Contact List -----")

            for name , phone in contact.items():

                print("Name :" ,name)
                print("Phone" , phone)
                print("-----------------------")

    # search Contact

    if choice == "3":

      name=input("Enter the number : ")

      if name in contact:
          print("name" , name)
          print("phone" , contact[name])
      else:
          print("contact not found : ")

    # delete Contact

    if choice == "4":

        name = input("Enter the name to delete : ")

        try :

            del contact[name]
            print("delete successfully")
        except KeyError :
            print("Contact not found.")

    # Exit 

    elif choice == "5" :

        print("Thank you for using Contact Management System!")

        break
    



# contacts = {}


# while True:

#     print("\n===== CONTACT MANAGEMENT SYSTEM =====")
#     print("1. Add Contact")
#     print("2. View Contacts")
#     print("3. Search Contact")
#     print("4. Delete Contact")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     # Add Contact
#     if choice == "1":

#         name = input("Enter name: ")
#         phone = input("Enter phone number: ")

#         contacts[name] = phone

#         print("Contact added successfully!")


#     # View Contacts
#     elif choice == "2":

#         if len(contacts) == 0:
#             print("No contacts found.")

#         else:
#             print("\n----- Contact List -----")

#             for name, phone in contacts.items():
#                 print("Name:", name)
#                 print("Phone:", phone)
#                 print("------------------------")


#     # Search Contact
#     elif choice == "3":

#         name = input("Enter name to search: ")

#         if name in contacts:
#             print("Name:", name)
#             print("Phone:", contacts[name])

#         else:
#             print("Contact not found.")


#     # Delete Contact
#     elif choice == "4":

#         name = input("Enter name to delete: ")

#         try:
#             del contacts[name]
#             print("Contact deleted successfully!")

#         except KeyError:
#             print("Contact not found.")


#     # Exit
#     elif choice == "5":

#         print("Thank you for using Contact Management System!")
#         break


#     else:
#         print("Invalid choice. Please try again.")

    



