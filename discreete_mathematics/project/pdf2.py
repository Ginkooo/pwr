from itertools import count, islice
from random import choice, randint


distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}


def distance_generator():
    pow_gen = (10**i for i in islice(count(1), 4))
    for node_count in pow_gen:
        nodes = [x for x in range(node_count)]
        distances = {}
        for node in nodes:
            distances[node] = {choice(nodes): randint(1, 10) for _ in range(int(len(nodes) * 0.2))}
        print('dupa')
        yield distances

for distances in distance_generator():
    continue

    nodes = tuple(sorted(tuple(distances)))


    unvisited = {node: None for node in nodes}
    visited = {}
    current = 0
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited:
                continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

    print(visited)
