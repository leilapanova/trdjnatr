class Retailitem:
    def __init__(self, name, desc, col_v, price):
        self.name = name
        self.desc = desc
        self.col_v = col_v
        self.price = price

    def __str__(self):
        return f'{self.desc}.{self.col_v}.{self.price}'


item1 = Retailitem('товар1', 'пиджак', 12, 59.95)
print(item1)
item2 = Retailitem('товар2', 'Джинсы', 40, 34.16)
print(item2)
item3 = Retailitem('товар3', 'рубашка', 20, 24.95)
print(item3)