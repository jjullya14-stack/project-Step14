from assistant.models import Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return str(error)
        except KeyError as error:
            return str(error)
        except IndexError:
            return "Not enough arguments."
        except TypeError:
            return "Invalid command format."

    return inner


def parse_input(user_input):
    if not user_input.strip():
        return "", []

    cmd, *args = user_input.split()
    return cmd.strip().lower(), args


@input_error
def add_contact(args, book):
    name, phone, *_ = args

    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)

    if record is None:
        raise KeyError("Contact not found.")

    record.edit_phone(old_phone, new_phone)
    return "Phone changed."


@input_error
def show_phone(args, book):
    name, *_ = args
    record = book.find(name)

    if record is None:
        raise KeyError("Contact not found.")

    phones = "; ".join(phone.value for phone in record.phones)
    return f"{name}: {phones}"


@input_error
def show_all(book):
    if not book.data:
        return "Address book is empty."

    return "\n".join(str(record) for record in book.data.values())


@input_error
def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)

    if record is None:
        raise KeyError("Contact not found.")

    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)

    if record is None:
        raise KeyError("Contact not found.")

    if record.birthday is None:
        return "Birthday not added."

    birthday = record.birthday.value.strftime("%d.%m.%Y")
    return f"{name}'s birthday: {birthday}"


@input_error
def birthdays(args, book):
    upcoming_birthdays = book.get_upcoming_birthdays()

    if not upcoming_birthdays:
        return "No upcoming birthdays."

    return "\n".join(
        f"{item['name']}: {item['congratulation_date']}"
        for item in upcoming_birthdays
    )

@input_error
def add_email(args, book):
    name, email, *_ = args
    record = book.find(name)

    if record is None:
        raise KeyError("Contact not found.")

    record.add_email(email)
    return "Email added."


@input_error
def show_email(args, book):
    name, *_ = args
    record = book.find(name)

    if record is None:
        raise KeyError("Contact not found.")

    if record.email is None:
        return "Email not added."

    return f"{name}'s email: {record.email.value}"


@input_error
def add_address(args, book):
    name, *address_parts = args
    record = book.find(name)

    if record is None:
        raise KeyError("Contact not found.")

    if not address_parts:
        raise ValueError("Address cannot be empty.")

    address = " ".join(address_parts)
    record.add_address(address)
    return "Address added."


@input_error
def show_address(args, book):
    name, *_ = args
    record = book.find(name)

    if record is None:
        raise KeyError("Contact not found.")

    if record.address is None:
        return "Address not added."

    return f"{name}'s address: {record.address.value}"

@input_error
def add_occasion(args, book):
    name, *occasion_parts = args
    record = book.find(name)

    if record is None:
        raise KeyError("Contact not found.")

    if not occasion_parts:
        raise ValueError("Occasion cannot be empty.")

    occasion = " ".join(occasion_parts)

    record.add_occasion(occasion)
    return "Occasion added."


@input_error
def show_occasions(args, book):
    name, *_ = args
    record = book.find(name)

    if record is None:
        raise KeyError("Contact not found.")

    return record.show_occasions()
