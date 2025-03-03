class Flowers:
    kind = 'Plants'

    def __init__(self, name, cost, freshness, size, life_time):
        self.name = name
        self.cost = cost
        self.freshness = freshness
        self.size = size
        self.life_time = life_time


class GardenFlowers(Flowers):
    type = 'Garden'
    color = 'Red'

    def __init__(self, name, cost, freshness, size, life_time):
        super().__init__(name, cost, freshness, size, life_time)


class WildFlowers(Flowers):
    type = 'Wild'
    color = 'Yellow'

    def __init__(self, name, cost, freshness, size, life_time):
        super().__init__(name, cost, freshness, size, life_time)


class ForestFlowers(Flowers):
    type = 'Forest'
    color = 'Green'

    def __init__(self, name, cost, freshness, size, life_time):
        super().__init__(name, cost, freshness, size, life_time)


class BouquetFlowers:

    def __init__(self, *flower):
        self.list_flowers = list(flower)

    def wilting_time(self):
        a = []
        for flower in self.list_flowers:
            a.append(flower.life_time)
        print(sum(a) / len(self.list_flowers))

    def sort_size(self):
        a = []
        for flower in self.list_flowers:
            a.append(flower.size)
        print(sorted(a))

    def sort_freshness(self):
        a = []
        for flower in self.list_flowers:
            a.append(flower.freshness)
        print(sorted(a))

    def sort_cost(self):
        a = []
        for flower in self.list_flowers:
            a.append(flower.cost)
        print(sorted(a))

    def sort_color(self):
        a = []
        for flower in self.list_flowers:
            a.append(flower.color)
        print(sorted(a))

    def search_name(self):
        user_input = input('Enter a name:\n')
        found = False
        i = 0
        while i < len(self.list_flowers):
            if user_input == self.list_flowers[i].name:
                print(f'{user_input} in bouquet')
                found = True
                break
            i += 1
        if not found:
            print(f'{user_input} no in bouquet')


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
