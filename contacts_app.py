import json
CONTACTS_FILE = "contacts.json"
# Load contacts from file, or initialize to empty dict 
try:
    with open('contacts.json') as f:
        contacts = json.load(f) 
except FileNotFoundError:
    contacts = {}

def print_contacts():
    for name, contact in contacts.items():
        print(f"{name} - {contact['phone']} - {contact['email']}")

def add_contact():
    name = input("Name: ")
    phone = input("Phone number: ")
    email = input("Email address: ")
            
    contacts[name] = {'phone':phone, 'email':email}

def edit_contact():
    name = input("Name of contact to edit: ")
    if name in contacts:
        phone = input("New phone number (leave blank to unchanged): ")
        email = input("New email address (leave blank to unchanged): ")

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        
    else:
        print(f"Contact {name} not found.")
        
def delete_contact():
    name = input("Name of contact to delete: ")

    if name in contacts:
        del contacts[name]
    else:
        print(f"Contact {name} not found.")
        
def search_contacts():
    name = input("Search name: ")
    found = False
    for contact_name, contact in contacts.items():
        if name in contact_name:
            print(f"{contact_name} - {contact['phone']} - {contact['email']}")
            found = True
    
    if not found:
        print("No contacts matched your search.")

while True:
    print("1. Print contacts")
    print("2. Add contact")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Search contacts") 
    print("6. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print_contacts()
    elif choice == 2:
        add_contact()
    elif choice == 3:
        edit_contact()
    elif choice == 4:
        delete_contact()
    elif choice == 5:
        search_contacts()
    elif choice == 6:
        break

# Save contacts to file on exit  
with open('contacts.json', 'w') as f:
    json.dump(contacts, f)
    
print("Contacts saved to contacts.json.")
