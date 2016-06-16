from Search import city
from Search import bfs
from Search import dfs
from Search import ids


if __name__ == "__main__":
    print("=========================================")
    print("             Search Algorithms")
    print("=========================================")
    source = city.City(input("Enter the source city: ").capitalize(), '')
    destination = input("Enter the destination city: ").capitalize()
    algorithm = input("Enter the algorithm with which search has to be done: ").upper()
    if algorithm == "BFS":
        finder = bfs.BFS(source, destination)
        finder.find_route()
    elif algorithm == "DFS":
        finder = dfs.DFS(source, destination)
        finder.find_route()
    elif algorithm == "IDS":
        depth = int(input("Enter the depth for IDS: "))
        finder = ids.IDS(source, destination, depth)
        finder.find_route()
