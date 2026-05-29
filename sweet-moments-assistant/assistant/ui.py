def print_box(title, lines=None):
    if lines is None:
        lines = []

    width = 60

    print("╔" + "═" * width + "╗")
    print(f"║ {title:<58} ║")

    if lines:
        print("╠" + "═" * width + "╣")
        for line in lines:
            print(f"║ {line:<58} ║")

    print("╚" + "═" * width + "╝")


def show_main_menu():
    print_box(
        "🎂 SWEET MOMENTS ASSISTANT",
        [
            "help - show all commands",
            "add - add new client",
            "all - show all clients",
            "find-contact - search client",
            "find-note - search note",
            "find-tag - search tag",
            "exit - save and close",
        ],
    )


def show_help():
    print_box(
        "📌 AVAILABLE COMMANDS",
        [
            "add [name] [+phone]",
            "add-email [name] [email]",
            "add-address [name] [address]",
            "add-birthday [name] [DD.MM.YYYY]",
            "add-note [name] [text]",
            "add-tag [name] [tag]",
            "find-contact [text]",
            "find-note [text]",
            "find-tag [tag]",
            "all",
            "exit / close",
        ],
    )
    