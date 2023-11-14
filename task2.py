from dataclasses import dataclass
@dataclass
class Book:

        title: str
        name:str
        author:str
    def get_title(self):
        return self.title

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def set_title(self, title):
        self.title = title

    def set_name(self, name):
        self.name = name

    def set_author(self, author):
        self.author = author

    def __str__(self):
        return f'Заголовок {self.title}'

a = Book('Колобок', 'Русалка', 'Народные')
print(a.get_title())
print(a.get_name())
print(a.get_author)
