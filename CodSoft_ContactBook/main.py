# Define the contact list
contact_list = []


# Main Menu
def main_menu():
	while True:
		print("\n--- Contact Book Menu ---")
		print("1. Add Contact")
		print("2. View Contact List")
		print("3. Search Contact")
		print("4. Update Contact")
		print("5. Delete Contact")
		print("6. Exit")

		choice = input("Enter your choice: ")

		if choice == "1":
			add_contact()
		elif choice == "2":
			view_contacts()
		elif choice == "3":
			search_contact()
		elif choice == "4":
			update_contact()
		elif choice == "5":
			delete_contact()
		elif choice == "6":
			print("Goodbye!")
			break
		else:
			print("Invalid choice. Please try again.")


# Add Contact
def add_contact():
	print("\n--- Add New Contact ---")
	name = input("Enter Name: ").strip()
	phone = input("Enter Phone Number: ").strip()
	email = input("Enter Email: ").strip()
	address = input("Enter Address: ").strip()

	if not name or not phone:
		print("Name and Phone Number are required!")
		return

	contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
	contact_list.append(contact)
	print(f"Contact '{name}' added successfully!")


# View Contact List
def view_contacts():
	print("\n--- Contact List ---")
	if not contact_list:
		print("No contacts available.")
		return

	for idx, contact in enumerate(contact_list, start=1):
		print(f"{idx}. {contact['Name']} - {contact['Phone']}")


# Search Contact
def search_contact():
	print("\n--- Search Contact ---")
	term = input("Enter Name or Phone to search: ").strip()

	results = [c for c in contact_list if term in c['Name'] or term in c['Phone']]
	if results:
		print("Search Results:")
		for contact in results:
			display_contact(contact)
	else:
		print("No matching contacts found.")


# Display Contact Details
def display_contact(contact):
	print("\n--- Contact Details ---")
	print(f"Name: {contact['Name']}")
	print(f"Phone: {contact['Phone']}")
	print(f"Email: {contact['Email']}")
	print(f"Address: {contact['Address']}")


# Update Contact
def update_contact():
	print("\n--- Update Contact ---")
	term = input("Enter Name or Phone to update: ").strip()

	for contact in contact_list:
		if term == contact['Name'] or term == contact['Phone']:
			print("Current Details:")
			display_contact(contact)

			print("\nEnter new details (leave blank to keep current):")
			contact['Name'] = input(f"Name ({contact['Name']}): ").strip() or contact['Name']
			contact['Phone'] = input(f"Phone ({contact['Phone']}): ").strip() or contact['Phone']
			contact['Email'] = input(f"Email ({contact['Email']}): ").strip() or contact['Email']
			contact['Address'] = input(f"Address ({contact['Address']}): ").strip() or contact['Address']

			print("Contact updated successfully!")
			return

	print("Contact not found.")


# Delete Contact
def delete_contact():
	print("\n--- Delete Contact ---")
	term = input("Enter Name or Phone to delete: ").strip()

	for contact in contact_list:
		if term == contact['Name'] or term == contact['Phone']:
			print("Contact to delete:")
			display_contact(contact)

			confirm = input("Are you sure? (yes/no): ").strip().lower()
			if confirm == "yes":
				contact_list.remove(contact)
				print("Contact deleted successfully!")
				return

	print("Contact not found.")


# Run the application
if __name__ == "__main__":
	main_menu()
