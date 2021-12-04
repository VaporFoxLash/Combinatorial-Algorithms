# Radebe, task2

def is_bipartite(adj, v, visited, color):
    for neighbor in adj[v]:
        if not visited[neighbor]:
            visited[neighbor] = True

            color[neighbor] = not color[v]
            if not is_bipartite(adj, neighbor,
                                visited, color):
                return False
        elif color[neighbor] == color[v]:
            return False

    return True


def main():
    lines = []
    with open('input.txt', 'r') as f:
        for line in f:
            lines.append(line)

    N = int(lines[0])
    visited = [0 for _ in range(N + 1)]
    color = [0 for _ in range(N + 1)]
    adj_matrix = [[0] for _ in range(1)]

    for i in range(1, N + 1):
        adj_matrix.append([int(x) for x in lines[i].split()])

    visited[1] = True
    color[1] = False
    if is_bipartite(adj_matrix, 1, visited, color):
        print("Y")
    else:
        print("N")
    set_a = set()
    set_b = set()
    for i in range(1, len(color)):
        if color[i]:
            set_a.add(i)
        else:
            set_b.add(i)
    print(set_b)
    print(set_a)


if __name__ == '__main__':
    main()
