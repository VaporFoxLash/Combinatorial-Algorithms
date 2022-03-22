import math


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def checkPath(self, dist, src, goal):
        if math.isinf(dist[goal]):
            print("N")
        else:
            print("Y")

    def BellmanFord(self, src, goal):
        dist = [math.inf] * self.V
        dist[src] = 0
        path = list()
        # path.append(src)

        for _ in range(1, self.V - 1):
            for u, v, w in self.graph:
                if not math.isinf(dist[u]) and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

                    if u not in path:
                        path.append(u)

                    if v not in path:
                        path.append(v)

        for u, v, w in self.graph:
            if not math.isinf(dist[u]) and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        self.checkPath(dist, src, goal)
        sol = ' '.join(str(e) for e in path)
        print(sol)
        print(dist[goal])


def createGraph(matrix, N):
    vertices = []
    weights = []
    nodes = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - 1):
            if j % 2 == 0:
                vertices.append(matrix[i][j])
                nodes.append(i + 1)
            else:
                weights.append(matrix[i][j])

    g = Graph(N + 1)
    for i in range(len(weights)):
        g.addEdge(nodes[i], vertices[i], weights[i])

    return g


def main():
    lines = []
    with open('in.txt', 'r') as f:
        for line in f:
            lines.append(line)

    N = int(lines[0])
    src = int(lines[N + 1])
    goal = int(lines[N + 2])

    g = Graph(N)
    adj_matrix = []

    for i in range(1, N + 1):
        adj_matrix.append([int(x) for x in lines[i].split()])

    g = createGraph(adj_matrix, N)
    # print(g.graph)
    g.BellmanFord(src, goal)


if __name__ == '__main__':
    main()
