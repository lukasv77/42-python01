#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float) -> None:
        self.name = name
        self.growth_rate = growth_rate
        self._height = 0.0
        self._age_days = 0
        if self._is_valid_height(height):
            self._height = height
        if self._is_valid_age(age_days):
            self._age_days = age_days

    def _is_valid_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        return True

    def _is_valid_age(self, age_days: int) -> bool:
        if age_days < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def show(self) -> None:
        print(f'{self.name}: {self._height}cm, {self._age_days} days old')

    def grow(self) -> None:
        self._height = round(self._height + self.growth_rate, 1)

    def age(self) -> None:
        self._age_days += 1

    def set_height(self, height: float) -> bool:
        if not self._is_valid_height(height):
            print("Height update rejected")
            return False
        self._height = height
        print(f"Height updated: {round(self._height, 1)}cm")
        return True

    def set_age(self, age_days: int) -> bool:
        if not self._is_valid_age(age_days):
            print("Age update rejected")
            return False
        self._age_days = age_days
        print(f"Age updated: {self._age_days} days")
        return True


class Flower(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float, color: str) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f' Color: {self.color}')
        if self.bloomed is False:
            print(f' {self.name} has not bloomed yet')
        else:
            print(f' {self.name} is blooming beautifully!')


class Tree(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f'Tree {self.name} now produces a shade of {self._height}cm long'
              f' and {self.trunk_diameter}cm wide.')

    def show(self) -> None:
        super().show()
        print(f' Trunk diameter: {self.trunk_diameter}cm')


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float, harvest_season: str) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f' Harvest season: {self.harvest_season}')
        print(f' Nutritional value: {round(self.nutritional_value)}')


if __name__ == '__main__':
    rose = Flower('Rose', 15.0, 10, 0.8, 'red')
    oak = Tree('Oak', 200.0, 365, 0.8, 5.0)
    tomato = Vegetable('Tomato', 5.0, 10, 2.1, 'April')

    print('=== Garden Plant Types ===\n'
          '=== Flower')
    rose.show()
    print('[asking the rose to bloom]')
    rose.bloom()
    rose.show()
    print('\n=== Tree')
    oak.show()
    print('[asking the oak to produce shade]')
    oak.produce_shade()
    print('\n=== Vegetable')
    tomato.show()
    print('[make tomato grow and age for 20 days]')
    for i in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
