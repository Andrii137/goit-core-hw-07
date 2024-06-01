from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field): 
    def __init__(self, name):
        if not name:
            raise ValueError("Name must not be empty.")
        super().__init__(name)

class Phone(Field): 
    def __init__(self, phone):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Phone number must have 10 digits.")
        super().__init__(phone)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record: 
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                self.phones.remove(ph)

    def edit_phone(self, old_phone, new_phone):
        phone_exists = False
        for p in self.phones:
            if p.value == old_phone:
                phone_exists = True
                break

        if not phone_exists:
            raise ValueError("Phone number to edit does not exist.")

        if not new_phone.isdigit() or len(new_phone) != 10:
            raise ValueError("New phone number must be a 10-digit number.")

        for ph in self.phones:
            if ph.value == old_phone:
                ph.value = new_phone

    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None
    def __str__(self):
        birthday_str = str(self.birthday.value.strftime("%d.%m.%Y")) if self.birthday else 'Not specified'
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Name not found")
        
    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []
        for user in self.data.values():
            if user.birthday:
                birthday_this_year = datetime(today.year, user.birthday.value.month, user.birthday.value.day).date()
                if birthday_this_year < today:
                    continue
                elif (birthday_this_year - today).days < 7:
                    if birthday_this_year.weekday() == 5:
                        birthday_this_year += timedelta(days=2)
                    elif birthday_this_year.weekday() == 6:
                        birthday_this_year += timedelta(days=1)
                    user_info = {"name": user.name.value, "congratulation_date": birthday_this_year.strftime("%d.%m.%Y")}
                    upcoming_birthdays.append(user_info)
        return upcoming_birthdays
    
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This command cannot be executed."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "There is no such information."
        except Exception as e:
            return f"Error: {e}"
    return inner


@input_error
def add_birthday(args, book):
    # реалізація

@input_error
def show_birthday(args, book):
    # реалізація

@input_error
def birthdays(args, book):
    # реалізація

  