from heapq import heapify


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the problem statement
    return: cost (int) minimum cost of connecting all islands
    TODO complete this method to returh minimum cost of connecting all islands
    """
    import heapq
    graph = {}
    cost = 0
    visited = set()
    adj_matrix = []
    index = 0  # island
    heap = []
    heapq.heapify(heap)

    for config in bridge_config:
        if not graph.get(config[0]):
            graph[config[0]] = [(config[2], config[1])]
        else:
            l = graph.get(config[0])
            l.append((config[2], config[1]))

        if not graph.get(config[1]):
            graph[config[1]] = [(config[2], config[0])]
        else:
            l = graph.get(config[1])
            l.append((config[2], config[0]))

    for i in range(0, num_islands + 1):
        if i == 0:
            adj_matrix += [[]]
        else:
            if graph.get(i):
                adj_matrix += [graph[i]]

    for i in range(0, len(adj_matrix)):
        if len(adj_matrix[i]) != 0:
            index = i
            break


    while len(visited) != num_islands-1:
        visited.add(index)
        for vertex in adj_matrix[index]:
            heapq.heappush(heap, vertex)

        smallest = heapq.heappop(heap)
        while smallest[1] in visited:
            if len(heap) != 0:
                smallest = heapq.heappop(heap)
        cost += smallest[0]
        index = smallest[1]

    return cost


num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]

print("Minimum cost", get_minimum_cost_of_connecting(num_islands, bridge_config))  # 6