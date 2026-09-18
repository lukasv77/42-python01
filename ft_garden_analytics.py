#!/usr/bin/env python3

class Plant:

    class Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def get_grow_calls(self) -> int:
            return self._grow_calls

        def get_age_calls(self) -> int:
            return self._age_calls

        def get_show_calls(self) -> int:
            return self._show_calls

        def add_grow_call(self) -> None:
            self._grow_calls += 1

        def add_age_call(self) -> None:
            self._age_calls += 1

        def add_show_call(self) -> None:
            self._show_calls += 1

        def show_stats(self) -> None:
            print(f'Stats: {self.get_grow_calls()} grow, '
                  f'{self.get_age_calls()} age, {self.get_show_calls()} show')

    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float) -> None:
        self.name = name
        self._height = height
        self._age_days = age_days
        self.growth_rate = growth_rate
        self._stats = Plant.Statistics()

    def show(self) -> None:
        print(f'{self.name}: {self._height}cm, {self._age_days} days old')
        self._stats.add_show_call()

    def grow(self) -> None:
        self._height = round(self._height + self.growth_rate, 1)
        self._stats.add_grow_call()

    def age(self) -> None:
        self._age_days += 1
        self._stats.add_age_call()

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

    @staticmethod
    def is_more_than_year(days: int) -> bool:
        if days > 365:
            return True
        else:
            return False

    @classmethod
    def anonymous(cls):
        return cls('Unknown plant', 0.0, 0, 0.0)


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
    class TreeStatistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def get_shade_calls(self) -> int:
            return self._shade_calls

        def add_shade_call(self) -> None:
            self._shade_calls += 1

        def show_stats(self) -> None:
            super().show_stats()
            print(f' {self.get_shade_calls()} shade')

    _stats: TreeStatistics

    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.trunk_diameter = trunk_diameter
        self._stats = Tree.TreeStatistics()

    def produce_shade(self) -> None:
        print(f'Tree {self.name} now produces a shade of {self._height}cm long'
              f' and {self.trunk_diameter}cm wide.')
        self._stats.add_shade_call()

    def show(self) -> None:
        super().show()
        print(f' Trunk diameter: {self.trunk_diameter}cm')


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float, harvest_season: str,
                 nutritional_value: float) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

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


class Seed(Flower):
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float, color: str, seeds: int) -> None:
        super().__init__(name, height, age_days,
                         growth_rate, color)
        self.seeds_nb = seeds

    def bloom(self) -> None:
        super().bloom()
        self.seeds_nb = 42

    def show(self) -> None:
        super().show()
        print(f' Seeds: {self.seeds_nb}')


def print_stats(obj: Plant) -> None:
    obj._stats.show_stats()


if __name__ == '__main__':
    rose = Flower('Rose', 15.0, 10, 8, 'red')
    oak = Tree('Oak', 200.0, 365, 0.8, 5.0)
    sunflower = Seed('Sunflower', 80.0, 45, 1.5, 'yellow', 0)

    print('=== Garden statistics ===\n'
          '=== Check year-old')
    print(f'Is 30 days more than a year? -> {Plant.is_more_than_year(30)}')
    print(f'Is 400 days more than a year? -> {Plant.is_more_than_year(400)}')
    print('\n=== Flower')
    rose.show()
    print('[statistics for Rose]')
    print_stats(rose)
    print('[asking the rose to grow and bloom]')
    rose.grow()
    rose.bloom()
    rose.show()
    print('[statistics for Rose]')
    print_stats(rose)
    print('\n=== Tree')
    oak.show()
    print('[statistics for Oak]')
    print_stats(oak)
    print('[asking the oak to produce shade]')
    oak.produce_shade()
    print('[statistics for Oak]')
    print_stats(oak)
    print('\n=== Seed')
    sunflower.show()
    print('[make sunflower grow, age and bloom]')
    for i in range(20):
        sunflower.grow()
        sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print('[statistics for Sunflower]')
    print_stats(sunflower)
    print('\n=== Anonymous')
    unknown_plant = Plant.anonymous()
    unknown_plant.show()
    print('[statistics for Unknown plant]')
    print_stats(unknown_plant)
