from dataclasses import dataclass

@dataclass
class Employee:
    def init(self, name, number_id, departament, job):
        self.name = name
        self.number_id = number_id
        self.departament = departament
        self.job = job

    def str(self):
        return f'{self.name},{self.number_id},{self.departament},{self.job}'


chel = Employee('Сьюзан Мейерс', '47899', 'Бухгалерия','Вице-президент')
print(chel)
chel2 = Employee('Марк Джоунс', '39119', 'ИТ','Программист')
print(chel2)
chel3 = Employee('Джой Роджерс', '81774', 'Производственный ','Инженер')
print(chel3)