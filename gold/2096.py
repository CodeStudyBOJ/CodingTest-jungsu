N = int(input())

points = [list(map(int, input().split())) for _ in range(N)]

dp = [[0,0] for _ in range(3)]

for i in range(N):
    dp[0][0], dp[0][1], dp[1][0], dp[1][1], dp[2][0], dp[2][1] = points[i][0] + max(dp[0][0], dp[1][0]) , points[i][0] + min(dp[0][1], dp[1][1]) , points[i][1] + max(dp[0][0], dp[1][0], dp[2][0]), points[i][1] + min(dp[0][1], dp[1][1], dp[2][1]), points[i][2] + max(dp[1][0], dp[2][0]), points[i][2] + min(dp[1][1], dp[2][1])


print(max(dp[i][0] for i in range(3)), min(dp[i][1] for i in range(3)))
