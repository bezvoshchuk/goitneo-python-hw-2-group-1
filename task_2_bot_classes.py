from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    ...

class Phone(Field):
    def validate(self, value):
        return re.match(r'(\+[0-9]+\s*)?(\([0-9]+\))?[\s0-9\-]+[0-9]+', value)

class Record:
    def __init__(self, name: Name, phone: Phone):
        self.name = name
        self.phones = [phone]

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        self.phones.remove(old_phone)
        self.phones.append(new_phone)

    def find_phone(self, name: Name):
        self.name = name
        if self.name:
            return self.phones

    def remove_phone(self, phone: Phone):
        self.phones.remove(phone)

    def __str__(self):
        return f"Record | contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self[record.name.value] = record

    def find(self, name: Name):
        if name.value in list(self.keys()):
            return self[name.value]

    def delete(self, name: Name):
        del self.data[name]
