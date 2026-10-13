TABLE_SIZE = 10


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name} | Phone: {self.phone} | Email: {self.email}"


class PhoneBook:
    def __init__(self):
        self.table = [None] * TABLE_SIZE
        self.deleted = object()

    # --------------------------------------------------------
    # Hash Function
    # --------------------------------------------------------
    def hash_function(self, phone):
        return sum(ord(char) for char in phone) % TABLE_SIZE

    # --------------------------------------------------------
    # Find index using Linear Probing
    # --------------------------------------------------------
    def find_index(self, phone):
        index = self.hash_function(phone)

        for _ in range(TABLE_SIZE):
            item = self.table[index]

            if item is None:
                return None

            if item is not self.deleted and item.phone == phone:
                return index

            index = (index + 1) % TABLE_SIZE

        return None

    # --------------------------------------------------------
    # Add Contact
    # --------------------------------------------------------
    def add_contact(self, name, phone, email):
        # Check whether contact already exists
        if self.find_index(phone) is not None:
            print("\nContact with this phone number already exists.")
            return

        index = self.hash_function(phone)
        original_index = index

        for _ in range(TABLE_SIZE):
            if self.table[index] is None or self.table[index] is self.deleted:
                self.table[index] = Contact(name, phone, email)

                print("\nContact added successfully!")
                print(f"Hash Index : {original_index}")
                print(f"Stored At  : {index}")

                if original_index != index:
                    print("Collision handled using Linear Probing.")

                return

            index = (index + 1) % TABLE_SIZE

        print("\nPhonebook is full!")

    # --------------------------------------------------------
    # Search Contact
    # --------------------------------------------------------
    def search_contact(self, phone):
        index = self.find_index(phone)

        if index is not None:
            print("\nContact Found!")
            print("--------------------------------")
            print(self.table[index])
            print(f"Hash Index : {self.hash_function(phone)}")
            print(f"Stored At  : {index}")
            return

        print("\nContact not found.")

    # --------------------------------------------------------
    # Update Contact
    # --------------------------------------------------------
    def update_contact(self, phone):
        index = self.find_index(phone)

        if index is None:
            print("\nContact not found.")
            return

        print("\nCurrent Contact:")
        print(self.table[index])

        name = input("Enter new name: ").strip()
        email = input("Enter new email: ").strip()

        if name:
            self.table[index].name = name

        if email:
            self.table[index].email = email

        print("\nContact updated successfully!")

    # --------------------------------------------------------
    # Delete Contact
    # --------------------------------------------------------
    def delete_contact(self, phone):
        index = self.find_index(phone)

        if index is None:
            print("\nContact not found.")
            return

        self.table[index] = self.deleted

        print("\nContact deleted successfully.")

    # --------------------------------------------------------
    # Display Phonebook
    # --------------------------------------------------------
    def display_contacts(self):
        print("\n")
        print("=" * 75)
        print("                    PHONEBOOK")
        print("=" * 75)

        found = False

        for index, contact in enumerate(self.table):

            if contact is None:
                print(f"Index {index:2} : Empty")

            elif contact is self.deleted:
                print(f"Index {index:2} : Deleted")

            else:
                found = True
                print(f"Index {index:2} : {contact}")

        print("=" * 75)

        if not found:
            print("Phonebook is empty.")

    # --------------------------------------------------------
    # Show Hash Information
    # --------------------------------------------------------
    def show_hash(self, phone):
        hash_index = self.hash_function(phone)

        print("\nHash Information")
        print("-----------------------------")
        print(f"Phone Number : {phone}")
        print(f"Hash Index   : {hash_index}")


# ============================================================
# Input Validation
# ============================================================

def get_phone():
    while True:
        phone = input("Enter phone number: ").strip()

        if phone.isdigit() and len(phone) >= 10:
            return phone

        print("Invalid phone number.")
        print("Please enter at least 10 digits.")


# ============================================================
# Main Program
# ============================================================

def main():

    phonebook = PhoneBook()

    while True:

        print("\n")
        print("=" * 50)
        print("       CUSTOM CONTACT PHONEBOOK")
        print("=" * 50)

        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Show Hash Index")
        print("7. Exit")

        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        # ----------------------------------------------------
        # Add
        # ----------------------------------------------------
        if choice == "1":

            print("\n--- Add New Contact ---")

            name = input("Enter name: ").strip()

            if not name:
                print("Name cannot be empty.")
                continue

            phone = get_phone()

            email = input("Enter email: ").strip()

            phonebook.add_contact(name, phone, email)

        # ----------------------------------------------------
        # Search
        # ----------------------------------------------------
        elif choice == "2":

            print("\n--- Search Contact ---")

            phone = get_phone()

            phonebook.search_contact(phone)

        # ----------------------------------------------------
        # Update
        # ----------------------------------------------------
        elif choice == "3":

            print("\n--- Update Contact ---")

            phone = get_phone()

            phonebook.update_contact(phone)

        # ----------------------------------------------------
        # Delete
        # ----------------------------------------------------
        elif choice == "4":

            print("\n--- Delete Contact ---")

            phone = get_phone()

            phonebook.delete_contact(phone)

        # ----------------------------------------------------
        # Display
        # ----------------------------------------------------
        elif choice == "5":

            phonebook.display_contacts()

        # ----------------------------------------------------
        # Hash
        # ----------------------------------------------------
        elif choice == "6":

            print("\n--- Hash Information ---")

            phone = get_phone()

            phonebook.show_hash(phone)

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------
        elif choice == "7":

            print("\nThank you for using Custom Contact Phonebook!")
            break

        else:

            print("\nInvalid choice. Please try again.")


# ============================================================
# Program Start
# ============================================================

if __name__ == "__main__":
    main()