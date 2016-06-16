from Search import search


class IDS(search.Search):
    def __init__(self, source, destination, depth):
        super(IDS, self).__init__(source, destination)
        self.depth_limit = depth
        self.limit = depth

    def find_route(self):
        visited_nodes = [self.source.name]
        if super(IDS, self).goal_check(self.source):
            print("You are already at destination")
        else:
            city_list = super(IDS, self).find_next_city(self.source, visited_nodes)
            path = []
            while len(city_list) != 0:
                city = city_list.pop()
                if city.level <= self.depth_limit:
                    visited_nodes.append(city.name)
                    if super(IDS, self).goal_check(city):
                        print("You have reached the destination", city.name)
                        path.append(city)
                        while city.parent != '':
                            path.append(super(IDS, self).find_parent(city))
                            city = city.parent
                        print("Path is: ")
                        for item in list(reversed(path)):
                            print(item.name)
                        i, distance = 0, 0
                        while i < len(path)-1:
                            distance += super(IDS, self).calculate_distance(path[i], path[i + 1])
                            i += 1
                        print("Distance is: ", distance)
                        break
                    else:
                        city_list.extend(super(IDS, self).find_next_city(city, visited_nodes))
                else:
                    print("Goal cannot be reached within this depth level ", self.depth_limit)
                    print("Increasing the depth level by one fold")
                    self.depth_limit += self.limit
