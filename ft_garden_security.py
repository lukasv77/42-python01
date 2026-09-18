#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float) -> None:
        self.name = name
        self._height = height
        self._age_days = age_days
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f'{self.name}: {self._height}cm, {self._age_days} days old')

    def grow(self) -> None:
        self._height = round(self._height + self.growth_rate, 1)

    def age(self) -> None:
        self._age_days += 1

    def set_height(self, height: float) -> bool:
        if height >= 0:
            self._height = height
            print(f'Height updated: {round(self._height)}cm')
            return (True)
        else:
            print(f"{self.name}: Error, height can't be negative\n"
                  f"Height update rejected")
            return (False)

    def set_age(self, age_days: int) -> bool:
        if age_days >= 0:
            self._age_days = age_days
            print(f'Age updated: {self._age_days} days')
            return (True)
        else:
            print(f"{self.name}: Error, age can't be negative\n"
                  f"Age update rejected")
            return (False)


if __name__ == '__main__':
    p1 = Plant('Rose', 15.0, 10, 0.8)
    print('=== Garden Security System ===')
    print('Plant created: ', end='')
    p1.show()
    print()
    p1.set_height(25.0)
    p1.set_age(30)
    print()
    p1.set_height(-25.0)
    p1.set_age(-30)
    print('\nCurrent state: ', end='')
    p1.show()
