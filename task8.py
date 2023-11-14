from dataclasses import dataclass, field
@dataclass
class Patient:
    adress: str
    town: str
    obl: str
    mail_index: str
    phone: list = field(default_factory=list)
    fio: list = field(default_factory=list)

    def get_adress(self):
        return self.adress
    def get_town(self):
        return self.adress
    def get_obl(self):
        return self.obl
    def get_mail_index(self):
        return self.mail_index
    def get_phone(self):
        return self.phone
    def get_fio(self):
        return self.fio

    def set_adress(self, adress):
        self.adress = adress
    def set_town(self, town):
        self.town = town
    def set_mail_index(self, mail_index)
        self.mail_index = mail_index
    def set_phone(self, phone):
        self.phone = phone
    def set_fio(self, fio):
        self.fio = fio

    def __repr__(self):
        return f'{self.adress},\n{self.town},\n{self.obl},\n{self.mail_index},\n{self.phone},\n{self.fio}'

class Procedure:
    def __init__(self, name_proc, date_proc, doctor, price):
        self.name_proc = name_proc
        self.date_proc = date_proc
        self.doctor = doctor
        self.price = price

    def get_name_proc(self):
        return self.name_proc
    def get_date_proc(self):
        return self.date_proc
    def get_doctor(self):
        return self.doctor
    def get_price(self):
        return self.price

    def set_name_proc(self, name_proc):
        self.name_proc = name_proc
    def set_date_proc(self, date_proc):
        self.date_proc = date_proc
    def set_doctor(self, doctor):
        self.doctor = doctor
    def set_price(self, price):
        self.price = price

    def __str__(self):
        return f'{self.name_proc},\n{self.date_proc},\n{self.doctor},\n{self.price}'


