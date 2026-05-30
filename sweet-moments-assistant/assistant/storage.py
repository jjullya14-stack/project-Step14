import pickle
from pathlib import Path

from assistant.address_book import AddressBook


# Шлях до файлу збереження даних
DATA_FILE = Path("data/addressbook.pkl")


# Збереження адресної книги у файл через pickle
def save_data(book, filename=DATA_FILE):
    filename.parent.mkdir(exist_ok=True)

    with open(filename, "wb") as file:
        pickle.dump(book, file)


# Завантаження даних з файлу
def load_data(filename=DATA_FILE):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)

    except FileNotFoundError:
        return AddressBook()