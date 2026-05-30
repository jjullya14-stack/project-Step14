from colorama import Fore, init

# Ініціалізація кольорового виводу в терміналі
init(autoreset=True)

# Створення красивої рамки для CLI
def print_box(title, lines=None):
    if lines is None:
        lines = []

    width = 60

    print(Fore.CYAN + "╔" + "═" * width + "╗")
    print(Fore.YELLOW + f"║ {title:<58} ║")

    if lines:
        print(Fore.CYAN + "╠" + "═" * width + "╣")
        for line in lines:
            print(Fore.WHITE + f"║ {line:<58} ║")

    print(Fore.CYAN + "╚" + "═" * width + "╝")

# Головне меню застосунку
def show_main_menu():
    print_box(
        "🎂 SWEET MOMENTS ASSISTANT",
        [
            "help - show all commands",
            "add - add new client",
            "all - show all clients",
            "birthdays - upcoming birthdays",
            "add-note - add client note",
            "add-tag - add client tag",
            "add-occasion - add family event",
            "find-contact - search client",
            "find-note - search note",
            "find-tag - search tag",
            "exit - save and close",
        ],
    )

# Відображення доступних команд
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
    