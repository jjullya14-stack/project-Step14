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


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.address = None
        self.birthday = None

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

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)

        email = self.email.value if self.email else "not added"
        address = self.address.value if self.address else "not added"

        if self.birthday:
            birthday = self.birthday.value.strftime("%d.%m.%Y")
        else:
            birthday = "not added"

        return (
            f"Contact name: {self.name.value}, "
            f"phones: {phones}, "
            f"email: {email}, "
            f"address: {address}, "
            f"birthday: {birthday}"
        )