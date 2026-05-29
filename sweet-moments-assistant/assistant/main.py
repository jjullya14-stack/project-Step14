from assistant.storage import load_data, save_data
from assistant.handlers import (
    parse_input,
    add_contact,
    change_contact,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
    add_email,
    show_email,
    add_address,
    show_address,
    add_occasion,
    show_occasions,
    add_note,
    show_notes,
)


def main():
    book = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))
            save_data(book)

        elif command == "change":
            print(change_contact(args, book))
            

        elif command == "phone":
            print(show_phone(args, book))
            
        elif command == "all":
            print(show_all(book))
            save_data(book)

        elif command == "add-birthday":
            print(add_birthday(args, book))
            
        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        elif command == "add-email":
            print(add_email(args, book))

        elif command == "show-email":
            print(show_email(args, book))

        elif command == "add-address":
            print(add_address(args, book))
            save_data(book)

        elif command == "show-address":
            print(show_address(args, book))

        elif command == "add-occasion":
            print(add_occasion(args, book))
            save_data(book)

        elif command == "show-occasions":
            print(show_occasions(args, book))

        elif command == "add-note":
            print(add_note(args, book))

        elif command == "show-notes":
            print(show_notes(args, book))    

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
