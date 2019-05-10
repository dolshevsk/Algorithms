graph = {}
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["finish"] = 3

graph["d"] = {}
graph["d"]["finish"] = 1

graph["finish"] = {}

costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = float('inf')
costs["d"] = float('inf')
costs["finish"] = float('inf')

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["finish"] = None

processed = []

def algotithm(costs):
    node = find_lowest(costs)

    while node is not None:
        node_cost = costs[node]
        neighbors = graph[node]
        for neighbor in neighbors:
            new_cost = node_cost + neighbors[neighbor]
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        processed.append(node)
        node = find_lowest(costs)
    return costs["finish"], parents["finish"]


def find_lowest(costs):
    lowest = float('inf')
    lowest_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest and node not in processed:
            lowest = cost
            lowest_node = node
    return lowest_node

print(algotithm(costs))
for x,y in parents.items():
    print(x, y) 