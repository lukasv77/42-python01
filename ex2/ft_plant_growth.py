#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f'{self.name}: {self.height}cm, {self.age_days} days old')

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.age_days += 1


if __name__ == '__main__':
    p1 = Plant('Rose', 25.0, 30, 0.8)
    start = p1.height
    print('=== Garden Plant Growth ===')
    p1.show()
    for i in range(7):
        p1.grow()
        p1.age()
        print(f'=== Day {i + 1} ===')
        p1.show()
    print(f'Growth this week: {round(p1.height - start, 1)}cm')
