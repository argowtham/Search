from Search_Algorithms import city
from Search_Algorithms import bfs
from Search_Algorithms import dfs
from Search_Algorithms import ids


if __name__ == "__main__":
    print("=========================================")
    print("             Search Algorithms")
    print("=========================================")
    source = city.City(input("Enter the source city: "), '')
    destination = input("Enter the destination city: ")
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
