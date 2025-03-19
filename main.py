from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        self.value = name

# class Phone & validation as a decorator
# def phone_validation(func):
#         def inner(phone:str)->str:
#             if len(phone) != 10 | (not phone.isdigit()):
#                 raise Exception("The phone number has to contain 10 digits")  
#             result = func(phone)
#             return result  
#         return inner
# @phone_validation    
# class Phone(Field):    
#     def __init__(self, phone):
#         self.value = phone
    
# class Phone & validation as a method
class Phone(Field):    
    def __init__(self, phone):
        self.value = self.phone_validation(phone)
    
    def phone_validation(self, phone):
        if len(phone) != 10 | (not phone.isdigit()):
            raise Exception("The phone number has to contain 10 digits")
        return phone
    
    
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if self.find_phone(phone):
            raise Exception(f"The phone number:{phone} has already been added.")
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        if not self.find_phone(phone):
            raise Exception(f"The phone number:{phone} is not found.")
        self.phones = [ph for ph in self.phones if ph.value != phone]   

    def edit_phone(self, phone, new_phone):
        if not self.find_phone(phone):
            raise Exception(f"The phone number:{phone} is not found.")
        self.phones = [Phone(new_phone) if ph.value == phone else ph for ph in self.phones]
        
    def find_phone(self, phone):
        result = [ph for ph in self.phones if ph.value == phone]
        return result[0] if len(result) > 0 else None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record):
        if record.name.value in self.data:
            raise Exception(f"The contact with name:{record.name.value} has already been added.")
        self.data[record.name.value] = record
            
    def find(self, name):
        result = self.data.get(name, None)
        if result == None:
            raise Exception(f"The contact with name:{name} is not found.")
        return result

    def delete(self, name):
        if not name in self.data:
            raise Exception(f"The contact with name:{name} is not found.")
        del self.data[name]
    


if __name__ == "__main__":
    try:
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
        print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

        # Видалення запису Jane
        book.delete("Jane")


        # Мої додаткові перевірки
        # Додавання та видалення телефону для John
        john_record.add_phone("1231231231")
        print(john) # Виведення: Contact name: John, phones: 1112223333; 5555555555; 1231231231
        john_record.remove_phone("1231231231")
        print(john) # Виведення: Contact name: John, phones: 1112223333; 5555555555
            
    except Exception as e:
    # Обробка будь-якого винятку
        print(f"An error occurred: {e}")
