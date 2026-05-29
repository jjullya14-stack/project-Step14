import pickle
from pathlib import Path

from assistant.address_book import AddressBook


DATA_FILE = Path("data/addressbook.pkl")


def save_data(book, filename=DATA_FILE):
    filename.parent.mkdir(exist_ok=True)

    with open(filename, "wb") as file:
        pickle.dump(book, file)


def load_data(filename=DATA_FILE):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()