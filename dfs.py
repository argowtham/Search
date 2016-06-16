from Search import search


class DFS(search.Search):
    def __init__(self, source, destination):
        super(DFS, self).__init__(source, destination)

    def find_route(self):
        visited_nodes = [self.source.name]
        if super(DFS, self).goal_check(self.source):
            print("You are already at destination")
        else:
            city_list = super(DFS, self).find_next_city(self.source, visited_nodes)
            path, final_path = [], []
            while len(city_list) != 0:
                city = city_list.pop()
                visited_nodes.append(city.name)
                if super(DFS, self).goal_check(city):
                    print("You have reached the destination", city.name)
                    path.append(city)
                    while city.parent != '':
                        path.append(super(DFS, self).find_parent(city))
                        city = city.parent
                    print("Path is: ")
                    for item in list(reversed(path)):
                        print(item.name)
                    i, distance = 0, 0
                    while i < len(path)-1:
                        distance += super(DFS, self).calculate_distance(path[i], path[i + 1])
                        i += 1
                    print("Distance is: ", distance)
                    break
                else:
                    city_list.extend(super(DFS, self).find_next_city(city, visited_nodes))
