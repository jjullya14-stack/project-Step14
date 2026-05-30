from assistant.models import Record


# Декоратор для обробки помилок введення користувача
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return str(error)
        except KeyError as error:
            return error.args[0]
        except IndexError:
            return "Not enough arguments."
        except TypeError:
            return "Invalid command format."

    return inner

# Розбір введеної команди на команду та аргументи
def parse_input(user_input):
    if not user_input.strip():
        return "", []

    cmd, *args = user_input.split()
    return cmd.strip().lower(), args


# Додавання або оновлення контакту
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


# Команди для роботи з днем народження
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

# Команди для роботи з email та адресою
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

# Команди для роботи з важливими подіями клієнта
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

# Команди для роботи з нотатками
@input_error
def add_note(args, book):
    name, *note_parts = args
    record = book.find(name)

    if record is None:
        raise KeyError("Contact not found.")

    if not note_parts:
        raise ValueError("Note cannot be empty.")

    note = " ".join(note_parts)
    record.add_note(note)
    return "Note added."


@input_error
def show_notes(args, book):
    name, *_ = args
    record = book.find(name)

    if record is None:
        raise KeyError("Contact not found.")

    return record.show_notes()

# Команди для роботи з тегами
@input_error
def add_tag(args, book):
    name, *tag_parts = args
    record = book.find(name)

    if record is None:
        raise KeyError("Contact not found.")

    if not tag_parts:
        raise ValueError("Tag cannot be empty.")

    tag = " ".join(tag_parts)

    record.add_tag(tag)
    return "Tag added."


@input_error
def show_tags(args, book):
    name, *_ = args
    record = book.find(name)

    if record is None:
        raise KeyError("Contact not found.")

    return record.show_tags()

# Пошук контактів, нотаток і тегів
@input_error
def find_contact(args, book):
    keyword, *_ = args

    result = book.search_contacts(keyword)

    if not result:
        return "No contacts found."

    return "\n".join(result)

@input_error
def find_note(args, book):
    keyword, *_ = args

    result = book.search_notes(keyword)

    if not result:
        return "No notes found."

    return "\n".join(result)

@input_error
def find_tag(args, book):
    keyword, *_ = args

    result = book.search_tags(keyword)

    if not result:
        return "No tags found."

    return "\n".join(result)

@input_error
def delete_contact(args, book):
    name, *_ = args

    book.delete(name)

    return "Contact deleted."
