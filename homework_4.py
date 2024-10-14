# Створив декоратор для кожної функції, як сказано у завданні, 
# хоча простіше і логічніше було би створити один універсальний декоратор по типу ось такого:

# def input_error(func):
#     def inner(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except ValueError:
#             return "Enter the argument for the command"
#         except IndexError:
#             return "Not enough arguments provided. Please check the command format."
#         except KeyError:
#             return "This contact does not exist."
#     return inner


# декоратор для додавання контактів
def input_error_add(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
    return inner

# декоратор пошуку телефонів
def input_error_phone(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Invalid data. Usage: phone <name>"
        except KeyError:
            return "Contact not found"
    return inner

# декортатор для зміни телефона
def input_error_change(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid data. Usage: change <name> <phone>"
        except KeyError:
            return "This contact does not exist."
    return inner

# декоратор для виведення всіх контактів
def input_error_all(func):
    def inner(dict):
        if dict:
            return func(dict)
        else:
            return "Phonebook is empty"
    return inner


# Парсинг командної строки
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@ input_error_add
def add_contact(args, contacts):
    name, phone = args # Очікуємо два аргументи: ім'я та телефон
    contacts[name] = phone
    return "Contact added."

@ input_error_change 
def change_contact(args, contacts):
    name, phone = args  # Очікуємо два аргументи
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        raise KeyError
    
@ input_error_phone 
def phone_username(args, contacts):
    username = args[0].strip()  # Отримуємо ім'я контакту
    return f"{username}'s phone is: {contacts[username]}"
    
  

@ input_error_all
def print_all(contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print(print_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
