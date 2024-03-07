from classes import Name, Phone, Record, AddressBook

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Please provide both name and phone number."
        except KeyError:
            return 'User does not exists.'
    return inner


def hello_command(args, contacts):
    return 'How can I help you?'

@input_error
def add_contact(args, contacts: AddressBook):
    name = Name(args[0])
    phone = Phone(args[1])
    contacts.add_record(Record(name, phone))
    return 'Contact was added.'

@input_error
def change_contact(args, contacts: AddressBook):
    name = Name(args[0])
    new_phone = Phone(args[1])

    old_record = contacts.find(name)
    if old_record:
        old_phone = old_record.phones[0]
        old_record.edit_phone(old_phone, new_phone)
        return 'Contact was changed.'
    else:
        return 'Such user does not exist.'
    
@input_error
def show_phone(args, contacts: AddressBook):
    name = args
    return contacts[name[0]]

def show_all(args, contacts: AddressBook):
    if (len(contacts) > 0):
        return str(contacts)
    else:
        return "No contacts found"

def exit_command(args, contacts):
    return 'Good bye!'

def list_commands(args, contacts):
    command_list = "Available commands:\n"
    for commands in COMMAND_HANDLER.values():
        command_list += ", ".join(commands) + "\n"
    return command_list

def unknown_command(args, contacts):
    return 'Unknown command. Use "list" to see all available commands.'

COMMAND_HANDLER = {
    hello_command: ['hello', 'hi', 'привіт'],
    add_contact: ['add', 'додати'],
    change_contact: ['change', 'змінити'],
    show_phone: ['phone', 'number', 'телефон', 'номер'],
    show_all: ['all', 'усі'],
    exit_command: ['exit', 'close', 'quit', 'q', 'вийти'],
    list_commands: ['list', 'команди']
}

def parser(user_input: str):
    for cmd, words in COMMAND_HANDLER.items():
        for word in words:
            if user_input.startswith(word):
                return cmd, user_input[len(word):].split()
    return unknown_command, []

def main():
    print('Welcome to phone assistant bot!')

    contacts = AddressBook()
    while True:
        user_input = input('Enter a command: ')
        cmd, data = parser(user_input)
        print(cmd(data, contacts))
        if cmd == exit_command:
            break

if __name__ == '__main__':
    main()