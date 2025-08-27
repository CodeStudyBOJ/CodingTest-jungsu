import heapq
import sys
input = sys.stdin.readline
V, E = map(int, input().split())

start = int(input())

edges = {}

for i in range(1, V+1):
    edges[i] = []

for _ in range(E):
    from_vertex, to_vertex, weight = map(int, input().split())
    edges[from_vertex].append((weight, to_vertex))

is_visited = [False] * (V+1)
is_visited[start] = True

ans = ['INF'] * V
ans[start-1] = 0

q = edges[start]
heapq.heapify(q)

while q:
    cur_weight, cur_vertex = heapq.heappop(q)
    if is_visited[cur_vertex]:
            continue
    is_visited[cur_vertex] = True
    ans[cur_vertex-1] = cur_weight    
    
    for val in edges[cur_vertex]:
        weight, vertex = val
        if is_visited[vertex]:
            continue
        heapq.heappush(q,(weight+cur_weight, vertex))


print(*ans, sep='\n')
