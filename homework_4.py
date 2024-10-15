# Декоратор для всіх функцій

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except IndexError:
            return "Not enough arguments provided. Please check the command format."
        except KeyError:
            return "This contact does not exist or phonebook is empty."
    return inner

# Парсинг командної строки
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args # Очікуємо два аргументи: ім'я та телефон
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args  # Очікуємо два аргументи
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        raise KeyError
    
@input_error 
def phone_username(args, contacts):
    username = args[0].strip()  # Отримуємо ім'я контакту
    return f"{username}'s phone is: {contacts[username]}"
  
@input_error
def print_all(contacts):
    if contacts:
        return contacts
    else:
        raise KeyError


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
