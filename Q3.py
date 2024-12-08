def search_contact(contacts, target_name):
    for contact in contacts:
        if contact['name'] == target_name:
            return f"Phone number found: {contact['phone']}"
    return "Contact not found."

contacts = [
    {"name": "Ana", "phone": "1234-5678"},
    {"name": "Carlos", "phone": "2345-6789"},
    {"name": "Bruna", "phone": "3456-7890"}
]

target_name = "Carlos"
result = search_contact(contacts, target_name)
print(result)
