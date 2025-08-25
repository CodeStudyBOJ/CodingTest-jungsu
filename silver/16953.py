INF = float('inf')

def recur(num, target, count):
    if num > target:
        return INF
    elif num == target:
        return count    
    return min(recur(num*10+1, target, count+1), recur(num*2, target, count+1))

n, target = map(int, input().split())

ans = recur(n, target, 0)

ans = -1 if ans == INF else ans+1

print(ans)

