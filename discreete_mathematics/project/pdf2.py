from itertools import count, islice
from random import choice, randint


def distance_generator():
    pow_gen = (10**i for i in islice(count(1), 3))
    for node_count in pow_gen:
        nodes = [x for x in range(node_count)]
        distances = {}
        for node in nodes:
            distances[node] = {choice(nodes): randint(1, 10) for _ in range(int(len(nodes) * 0.4))}
        yield distances


for distances in distance_generator():

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
