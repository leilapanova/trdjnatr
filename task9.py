class Employee:
    def __init__(self, name, number_id, office, work):
        self.name = name
        self.number_id = number_id
        self.office = office
        self.work = work

    def set_name(self, name):
        self.name = name
    def set_office(self, office):
        self.office = office
    def set_work(self, work):
        self.work = work

    def __str__(self):
        return f'{self.name}.{self.number_id}.{self.office}.{self.work}'

def e_list(key, value, dict):
    dict[key] = value
    return dict

def e_search(dict, name):
    res = {}
    for key  in dict:
        if name == dict[key].name:
            res =(dict[key])
    if res:
        print(dict[key])
    else:
        print('нет такого')
def e_change(name, office, work, Emp):
    Emp.set_name(name)
    Emp.set_office(office)
    Emp.set_work(work)

def e_delete(key, dict):
    del dict[key]

counter = 0
reestr = {}
chel = Employee('Сьюзан Мейерс', 7576, 'бухгалтерия', 'вице-Президент')
e_list(counter, chel, reestr)
counter += 1
chel2 = Employee('Марк Джоунс', 5445, 'IT', 'программист')
e_list(counter, chel2, reestr)
counter += 2
chel3 = Employee('джой роджерс', 5463, 'производственный', 'инжинер')
e_list(counter, chel3, reestr)

e_search(reestr, 'Марк Джоунс')
e_change('hdsxhag', 'sg5eg', 'sdfds', reestr[0])
print(reestr[0])
e_delete(0, reestr)
print(reestr[1])