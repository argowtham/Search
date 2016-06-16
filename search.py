from Search_Algorithms import city


class Search:
    def __init__(self, source_city, destination_city):
        self.source = source_city
        self.destination = destination_city

    def goal_check(self, current_city):
        if current_city.name == self.destination:
            return True
        else:
            return False

    def find_next_city(self, current_city, visited_nodes):
        next_city = []
        file = open("distance.csv", 'r')
        for line in file:
            line_array = line.split(',')
            if current_city.name in line_array:
                index = line_array.index(current_city.name)
                if index == 0 and line_array[1] not in visited_nodes:
                    next_city.append(city.City(line_array[1], current_city))
                else:
                    if line_array[0] not in visited_nodes:
                        next_city.append(city.City(line_array[0], current_city))
        file.close()
        return next_city

    def find_parent(self, current_city):
        return current_city.parent

    def calculate_distance(self, current_node, child_node):
        file = open("distance.csv", 'r')
        for line in file:
            if current_node.name in line and child_node.name in line:
                return int(line.split(',')[2])
