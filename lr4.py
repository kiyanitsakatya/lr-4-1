class Graph:
    def __init__(self):
        self.nodes = {}
    def add_node(self, value, weight=1):
        if value not in self.nodes:
            self.nodes[value] = {'weight': weight, 'edges': []}
    def add_edge(self, from_node, to_node):
        if from_node in self.nodes and to_node in self.nodes:
            self.nodes[from_node]['edges'].append(to_node)

def bfs_find_weight(graph, st, weight):
    visited = []
    q = [st]
    while q:
        node = q.pop(0)
        if node not in visited:
            visited.append(node)
            if graph.nodes[node]['weight'] == weight:
                return visited
            for neighbor in graph.nodes[node]['edges']:
                if neighbor not in visited:
                    q.append(neighbor)
    return visited

def dfs_find_weight(graph, st, weight):
    visited = []
    stack = [st]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if graph.nodes[node]['weight'] == weight:
                return visited
            for neighbor in reversed(graph.nodes[node]['edges']):
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

graph = Graph()
graph.add_node('A', 10)
graph.add_node('B', 12)
graph.add_node('C', 4)
graph.add_node('D', 3)
graph.add_node('E', 18)
graph.add_node('F', 6)
graph.add_node('G', 7)
graph.add_node('H', 11)
graph.add_node('I', 2)
graph.add_node('J', 8)

graph.add_edge("A", "J")
graph.add_edge("A", "C")
graph.add_edge("C", "F")
graph.add_edge("F", "G")
graph.add_edge("G", "H")
graph.add_edge("H", "C")
graph.add_edge("A", "B")
graph.add_edge("B", "E")
graph.add_edge("B", "D")
graph.add_edge("D", "I")

nums = [8, 2, 11, 7, 6, 18, 3, 4, 12, 10]

start = input("С какой вершины начнать?: ")
weight = int(input("Путь к какому значению ищем? "))
if weight not in nums:
    print('Нет такого значения')
else:
    print("Путь в ширину:", *bfs_find_weight(graph, start, weight))
    print("Путь в глубину:", *dfs_find_weight(graph, start, weight))