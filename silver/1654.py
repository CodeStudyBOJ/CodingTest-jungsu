def can_divide(loops, target_length, N):
    count = 0
    for loop in loops:
        count += (loop//target_length)
    return count >= N

def solution():
    K, N = map(int, input().split())

    loops = [int(input()) for _ in range(K)]
    
    left, right = 1, max(loops)

    ans = 0

    while left <= right:
        mid = (left+right) // 2
        if can_divide(loops, mid, N):
            ans = mid
            left = mid + 1
        else:
            right = mid -1
    print(ans)

solution()
