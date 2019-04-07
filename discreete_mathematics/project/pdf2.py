from random import choice, randint
from time import perf_counter

from matplotlib import pyplot as plt
from prettytable import PrettyTable


def distance_generator():
    counts = (10, 100, 200, 400, 600, 800, 1000)
    for node_count in counts:
        nodes = [x for x in range(node_count)]
        distances = {}
        for node in nodes:
            distances[node] = {choice(nodes): randint(1, 10) for _ in range(int(len(nodes) * 0.4))}
        yield distances


def dijkstra(distances):
    nodes = tuple(sorted(tuple(distances)))

    unvisited = {node: float('inf') for node in nodes}
    visited = {}
    current = 0
    current_distance = 0
    unvisited[current] = current_distance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited:
                continue
            new_distance = current_distance + distance
            if unvisited[neighbour] == float('inf') or unvisited[neighbour] > new_distance:
                unvisited[neighbour] = new_distance
        visited[current] = current_distance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]


def bellman_ford(graph):
    distance, predecessor = {}, {}
    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[0] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour], predecessor[neighbour] = distance[node] + graph[node][neighbour], node


djikstra_times = []
bell_times = []
counts = []
for distances in list(distance_generator()):
    counts.append(len(distances))

    start = perf_counter()
    dijkstra(distances)
    elapsed = perf_counter() - start
    djikstra_times.append(elapsed * 1000)

    start = perf_counter()
    bellman_ford(distances)
    elapsed = perf_counter() - start
    bell_times.append(elapsed * 1000)

times = PrettyTable()
times.field_names = ['Node count', 'Dijkstra [ms]', 'Bellman-Ford [ms]']
for row in zip(counts, djikstra_times, bell_times):
    times.add_row(row)

print(times)

print('Dikstra is O(|V|^2)')
print('Bellman-Ford is O(|V| * |E|)')

plt.title('Execution time comparation of Dijkstra and Bellman-Ford algo')
plt.plot(counts, djikstra_times, label='Dijkstra')
plt.plot(counts, bell_times, label='Bellman-Ford')
plt.yscale('log')
plt.ylabel('Time [ms]')
plt.xlabel('Node count')
plt.show()
