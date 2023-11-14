class information:
    def __init__(self, name, adress, age, phone_number):
        self.name = name
        self.adress = adress
        self.age = age
        self.phone_number = phone_number

    def get_name(self):
        return self.name
    def get_adress(self):
        return self.adress
    def get_age(self):
        return self.age
    def get_phone_number(self):
        return self.phone_number

    def __set_name__(self, name):
        self.name = name
    def set_adress(self, adress):
        self.adress = adress
    def set_age(self, age):
        self.age = age
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def __str__(self):
        return f'{self.name}, {self.adress}, {self.age}, {self.phone_number}'

personal_info = information('илья', 'ул Норд Дрфйв 7А', '23', 89648388932)
print(personal_info)
personal_info2 = information('паша', 'ул Норд Дрфйв 6А', '23', 89648388932)
print(personal_info2)
personal_info3 = information('гоша', 'ул Норд Дрфйв 5А', '23', 89648388932)
print(personal_info3)