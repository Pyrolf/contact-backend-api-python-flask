import uuid, json

class ContactService:
    def __init__(self, json_file):
        self.json_file = json_file
        self.load_contacts()

    def load_contacts(self):
        print(self.json_file)
        with open(self.json_file, "r") as file:
            self.contacts = json.load(file)

    def save_contacts(self):
        with open(self.json_file, "w") as file:
            json.dump(self.contacts, file)

    def is_email_or_phone_number_existed(self, email, phone_number):
        for contact in self.contacts:
            if contact["email"] == email or contact["phone_number"] == phone_number:
                return True
        return False

    def get_contact(self, id):
        for contact in self.contacts:
            if contact["_id"] == id:
                return contact

        return None
    
    def generate_id(self):
        while True:
            id = str(uuid.uuid4())
            contact = self.get_contact(id)
            if contact is None:
                return id
    
    def add_contact(self, app, name, email, phone):
        contact = {
            "_id": self.generate_id(),
            "name": name,
            "email": email,
            "phone_number": phone,
        }
        self.contacts.append(contact)
        if not app.config['TESTING']:
            self.save_contacts()
        return contact
