from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Contact not found.")

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            birthday = record.birthday.value
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days

            if 0 <= delta_days <= 7:
                congratulation_date = birthday_this_year

                if congratulation_date.weekday() == 5:
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:
                    congratulation_date += timedelta(days=1)

                upcoming_birthdays.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })

        return upcoming_birthdays
    
    def search_contacts(self, keyword):
        result = []

    def search_contacts(self, keyword):
        result = []

        for record in self.data.values():
            if keyword.lower() in record.name.value.lower():
                result.append(str(record))

        return result


    def search_notes(self, keyword):
        result = []

        for record in self.data.values():
            for note in record.notes:
                if keyword.lower() in note.value.lower():
                    result.append(str(record))
                    break

    def search_tags(self, keyword):
        result = []

        for record in self.data.values():
            if not hasattr(record, "tags"):
                continue

            for tag in record.tags:
                if keyword.lower() in tag.value.lower():
                    result.append(str(record))
                    break

        return result           

        