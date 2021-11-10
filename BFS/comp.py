from collections import deque as queue
import csv
import operator


lines = []
with open('input.txt', 'r') as f:
  for line in f:
    lines.append(line)


N = int(lines[0])
adj_matrix = []
visited = [False]*N
queue = []
comp_list = []
vertices = []


for i in range(1, N+1):
    adj_matrix.append([int(x) for x in lines[i].split()])


def BFS(v):
    visited[v] = 1
    queue.append(v+1)

    while (len(queue) > 0):
        vertices.append(queue.pop(0))

        for i in range(N):
            if adj_matrix[v][i] == 1 and not visited[i]:
                BFS(i)


my_graph = []
for i in range(N):
    for j in range(N):
        if adj_matrix[i][j] == 1:
            my_graph.append(sorted([i+1,j+1]))

my_graph = list(sorted(set(tuple(x) for x in my_graph)))


Ans = 0
results = []
for i in range(N):
    if not visited[i]:
        Ans += 1
        results.append([Ans,i+1])
        comp_list.append(Ans)

        BFS(i)

f = open("results.txt", "w")
for i in results:
    f.write(str(i[0]) +"---"+ str(i[1])+"\n0\n")
    print(str(i[0]) +"---"+ str(i[1]))
    print(0)
f.close()


# print(comp_list)
# print(my_graph)
# print(vertices)
