class City:
    def __init__(self, city_name, parent_city):
        self.name = city_name
        self.next_city = []
        self.parent = parent_city
        if parent_city == '':
            self.level = 1
        else:
            self.level = parent_city.level + 1
