from collections import deque

N = int(input())

edges ={}

for i in range(1, N+1):
    edges[i] = []

for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


ans = [0, 0] + [None for _ in range(N-1)]

q = deque([1])

while q:
    prev_vertex = q.popleft()

    for val in edges[prev_vertex]:
        if ans[val] == None:
            ans[val] = prev_vertex
            q.append(val)

for i in range(2, N+1):
    print(ans[i])

