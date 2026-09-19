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
