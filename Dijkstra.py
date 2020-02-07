from StringHelpers import reverse


def dijkstra(graph, initial, dest):
    """
    Run Dijkstra off of a given graph, initial node, and destination node
    """

    unvisited = []
    adjacency_list = {}
    path = {}

    for node in graph:
        adjacency_list[node] = float('inf')
        path[node] = None
        unvisited.append(node)

    adjacency_list[initial] = 0

    while unvisited:

        min_node = unvisited[0]
        min_value = adjacency_list[min_node]
        for n in range(1, len(unvisited)):

            if adjacency_list[unvisited[n]] < min_value:
                min_node = unvisited[n]
                min_value = adjacency_list[min_node]
        currentnode = min_node
        unvisited.remove(currentnode)

        visited = []
        visited.append(currentnode)

        for i in graph[currentnode]:
            alternate = graph[currentnode][i] + adjacency_list[currentnode]

            if adjacency_list[i] > alternate:

                adjacency_list[i] = alternate

                path[i] = currentnode

    x = dest
    result = []
    result.append(x)
    while True:
        x = path[x]
        if x is None:
            break
        result.append(x)
