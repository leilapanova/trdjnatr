from dataclasses import dataclass

@dataclass
class Car:
    def init(self, _year_model, rttake):
        self._year_model = _year_model
        self.rttake = rttake
        self._speed = 0

    def accelerate(self):
        self._speed += 5
        print(f'Скорость = {self._speed}')

    def breake(self):
        self._speed -= 5
        print(f'wwwc = {self._speed}')

    def get_speed(self):
        return self._speed


BMW = Car(2024, 'adf')
for i in range(5):
    BMW.accelerate()
    BMW.breake()

print(BMW.get_speed())