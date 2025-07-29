def add_contact(contacts, name, phone):
    if name in contacts:
        print(f"Контакт с именем {name} уже существует.")
    else:
        contacts[name] = phone
        print(f"Контакт {name} добавлен.")


def remove_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Контакт {name} удален.")
    else:
        print(f"Контакт с именем {name} не найден.")


def view_contacts(contacts):
    if contacts:
        print("Список контактов:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("Контактов нет.")

#основная функция.
def main():
    contacts = {}
    while True:
        print("\nТелефонная книга")
        print("1. Добавить контакт")
        print("2. Удалить контакт")
        print("3. Просмотреть контакты")
        print("4. Выйти")

        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            add_contact(contacts, name, phone)
        elif choice == '2':
            name = input("Введите имя для удаления: ")
            remove_contact(contacts, name)
        elif choice == '3':
            view_contacts(contacts)
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 4.")


if __name__ == "__main__":
    main()
