from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not self.is_valid_phone(value):
            raise ValueError("Phone must start with + and contain 10-15 digits.")
        super().__init__(value)

    @staticmethod
    def is_valid_phone(value):
        if not value.startswith("+"):
            return False

        digits = value[1:]
        return digits.isdigit() and 10 <= len(digits) <= 15


class Email(Field):
    def __init__(self, value):
        if not self.is_valid_email(value):
            raise ValueError("Invalid email format.")
        super().__init__(value)

    @staticmethod
    def is_valid_email(value):
        return "@" in value and "." in value


class Address(Field):
    pass


class Birthday(Field):
    def __init__(self, value):
        try:
            birthday_date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(birthday_date)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
class Occasion(Field):
    pass

class Note(Field):
    pass

class Tag(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.address = None
        self.birthday = None
        self.occasions = []
        self.notes = []
        self.notes = []
        self.tags = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_to_remove = self.find_phone(phone)

        if phone_to_remove:
            self.phones.remove(phone_to_remove)
        else:
            raise ValueError("Phone not found.")

    def edit_phone(self, old_phone, new_phone):
        phone_to_edit = self.find_phone(old_phone)

        if phone_to_edit:
            phone_to_edit.value = Phone(new_phone).value
        else:
            raise ValueError("Phone not found.")

    def find_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                return item
        return None

    def add_email(self, email):
        self.email = Email(email)

    def add_address(self, address):
        self.address = Address(address)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_occasion(self, occasion):
        if not hasattr(self, "occasions"):
            self.occasions = []

        self.occasions.append(Occasion(occasion))

    def show_occasions(self):
        if not hasattr(self, "occasions"):
            self.occasions = []

        if not self.occasions:
            return "No occasions added."

        return ", ".join(occasion.value for occasion in self.occasions)    

    def add_note(self, note):
        if not hasattr(self, "notes"):
            self.notes = []

        self.notes.append(Note(note))

    def show_notes(self):
        if not hasattr(self, "notes"):
            self.notes = []

        if not self.notes:
            return "No notes added."

        return "; ".join(note.value for note in self.notes)
    
    def add_tag(self, tag):
        if not hasattr(self, "tags"):
            self.tags = []

        self.tags.append(Tag(tag))

    def show_tags(self):
        if not hasattr(self, "tags"):
            self.tags = []

        if not self.tags:
            return "No tags added."

        return ", ".join(tag.value for tag in self.tags)


    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)

        email = self.email.value if self.email else "not added"
        address = self.address.value if self.address else "not added"
        occasions = self.show_occasions()

        if self.birthday:
            birthday = self.birthday.value.strftime("%d.%m.%Y")
        else:
            birthday = "not added"

        occasions = self.show_occasions()
        notes = self.show_notes()
        tags = self.show_tags()

        return (
            f"Contact name: {self.name.value}, "
            f"phones: {phones}, "
            f"email: {email}, "
            f"address: {address}, "
            f"birthday: {birthday}, "
            f"occasions: {occasions},"
            f"notes: {notes},"
            f"tags: {tags}"
)
    

    
