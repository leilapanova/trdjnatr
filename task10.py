from dataclasses import dataclass, field

@dataclass
class Retailitem:
    name: str
    discription: str
    kolvo: int
    price: float

    def __str__(self):
        return f'{self.name}.{self.discription}.{self.kolvo}.{self.price}'

@dataclass
class CashRegister:
    item_list: list = field(default_factory=list)

    def purchase_item(self, purches):
        self.item_list.append(purches)

    def get_total(self):
        total_summ = 0

    def show_items(self):
        for i in self.item_list:
            print(i)

    def clear_register(self):
        self.item_list = []

cash_register = CashRegister()
item1 = Retailitem('товар1', 'пиджак', 12, 59.95)
item2 = Retailitem('товар2', 'Джинсы', 40, 34.16)
item3 = Retailitem('товар3', 'рубашка', 20, 24.95)
#print(item1)
cash_register.purchase_item(item2)
cash_register.purchase_item(item1)
cash_register.show_items()
print(f'total: {cash_register.get_total()}')
cash_register.clear_register()
cash_register.show_items()