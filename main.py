from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    # реалізація класу
		pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.data.append(Phone(phone))

    def remove_phone(self, phone):
            self.phones = [ph for ph in self.phones if ph != phone]   

    def edit_phone(self, old_phone, new_phone):
        self.phones[self.phones.index(old_phone)] = new_phone
        
    def remove_phone(self, phone):
        result = [ph for ph in self.phones if ph != phone]   
        return result[0] if len(result) > 0 else None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    current_id = 1

    def __init__(self):
        self.records = []
    
    def add_record(self, record):
        self.data.append(Record({
                "id": AddressBook.current_id,
                "name": record.name,
                "phone": record.phone,
                "email": record.email,
            }
        ))
            
        AddressBook.current_id += 1

    def find(self, id):
            result = list(filter(lambda record: record.get("id") == id, self.records))
            return result[0] if len(result) > 0 else None

    def delete(self, name):
            result = list(filter(lambda record: record.get("name") != name, self.records))
            if len(result) != len(self.records):
                self.records = result        
            return 
    
if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")