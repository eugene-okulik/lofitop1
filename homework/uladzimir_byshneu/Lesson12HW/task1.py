class Flowers:
    kind = 'Plants'

    def __init__(self, name, cost, freshness, size, life_time, type, color):
        self.name = name
        self.cost = cost
        self.freshness = freshness
        self.size = size
        self.life_time = life_time
        self.type = type
        self.color = color


class GardenFlowers(Flowers):
    def __init__(self, name, cost, freshness, size, life_time):
        super().__init__(name, cost, freshness, size, life_time, type='Garden', color='Red')


class WildFlowers(Flowers):
    def __init__(self, name, cost, freshness, size, life_time):
        super().__init__(name, cost, freshness, size, life_time, type='Wild', color='Yellow')


class ForestFlowers(Flowers):
    def __init__(self, name, cost, freshness, size, life_time):
        super().__init__(name, cost, freshness, size, life_time, type='Forest', color='Green')


class BouquetFlowers:

    def __init__(self, *flower):
        self.list_flowers = list(flower)

    def wilting_time(self):
        a = []
        for flower in self.list_flowers:
            a.append(flower.life_time)
        print(f'Average wilting time: {sum(a) / len(self.list_flowers)}')

    def sort_size(self):
        sorted_flowers = sorted(self.list_flowers, key=lambda flower: flower.size)
        print("Sorted by size:")
        for flower in sorted_flowers:
            print(f'{flower.name}: {flower.size}')

    def sort_freshness(self):
        sorted_flowers = sorted(self.list_flowers, key=lambda flower: flower.freshness)
        print("Sorted by freshness:")
        for flower in sorted_flowers:
            print(f'{flower.name}: {flower.freshness}')

    def sort_cost(self):
        sorted_flowers = sorted(self.list_flowers, key=lambda flower: flower.cost)
        print("Sorted by cost:")
        for flower in sorted_flowers:
            print(f'{flower.name}: {flower.cost}')

    def sort_color(self):
        sorted_flowers = sorted(self.list_flowers, key=lambda flower: flower.color)
        print("Sorted by color:")
        for flower in sorted_flowers:
            print(f'{flower.name}: {flower.color}')

    def search_name(self):
        user_input = input('Enter a name:\n')
        found = False
        for flower in self.list_flowers:
            if user_input == flower.name:
                print(
                    f'Found: {flower.name}, Size: {flower.size}, Freshness: {flower.freshness}, '
                    f'Cost: {flower.cost}, Color: {flower.color}')
                found = True
                break
        if not found:
            print(f'{user_input} not found in bouquet')


flower1 = GardenFlowers('Rose', 10, 10, 5, 10)
flower2 = GardenFlowers('Peony', 6, 8, 10, 10)
flower3 = WildFlowers('Iris', 15, 11, 20, 15)
flower4 = WildFlowers('Gladiolus', 7, 9, 2, 15)
flower5 = ForestFlowers('Tulip', 5, 15, 15, 15)
flower6 = ForestFlowers('Aster', 6, 17, 21, 15)
bouquet1 = BouquetFlowers(flower1, flower3, flower6)
BouquetFlowers.wilting_time(bouquet1)
BouquetFlowers.sort_size(bouquet1)
BouquetFlowers.sort_cost(bouquet1)
BouquetFlowers.sort_freshness(bouquet1)
BouquetFlowers.sort_color(bouquet1)
BouquetFlowers.search_name(bouquet1)
