import sys
sys.setrecursionlimit(10**4+3)
input = sys.stdin.readline
def find_max_dist(target, edges):
    global ans
    first, second = 0, 0
    for val in edges[target]:
        vertex, weight = val
        cur_weight = find_max_dist(vertex, edges) + weight
        if cur_weight >= first:
            second = first
            first = cur_weight
        elif cur_weight > second:
            second = cur_weight
    ans = max(ans, first+second)
    return first

def solution():
    global ans
    N = int(input())

    edges = [[] for _ in range(N)]
    is_child = [False] * N
    for _ in range(N-1):
        parent, child, weight = map(int, input().split())
        is_child[child-1] = True
        edges[parent-1].append((child-1, weight))
    ans = 0
    root = 0
    for idx, val in enumerate(is_child):
        if val == False:
            root = idx
            break
    find_max_dist(root, edges)
    print(ans)

solution()
