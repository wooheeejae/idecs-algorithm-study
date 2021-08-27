# N개의 물건 존재
# 각 물건은 무게 W와 가치 V를 가진다.
# 가장은 최대 무게 K 가진다.

# W,V 주어진다.

import sys

# 무게 작은 순 sorting
# 무게 맞고, 최대 되게 더해서 dp 완성
# dp에서 가장 큰 것이 최대 무게

n,k = map(int,sys.stdin.readline().split())


dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
# dp[i][j] = 물건 무게 합 j 일 때, 처음 i 개의 아이템 중 담을 수 있는 최대 가치

# 현재 물건의 무게가 w 인데, j 즉 주어진 무게 보다 w 가 클 경우 담을 수 없으므로 이전 값 그대로 담는다.
# 현재 물건을 담지 않았을 때와 담았을 때, 가치를 비교해서 더 큰 값을 넣는다.

for i in range(1,n+1):
    w,v = map(int,sys.stdin.readline().split())
    # 무게마다 가격을 비교할 수 있도록 한다.
    for j in range(1,k+1):
        # 주어진 무게보다 입력한 무게가 더 클 경우
        if w > j:
            dp[i][j] = dp[i-1][j]
        # 주어진 무게가 가방 무게 보다 적어서 들어갈 수 있을 때
        else:
            # 해당 무게에서, 해당 물건을 더했을 때랑 안더했을 때 대소를 비교해서 넣는다.
            # 해당 무게에서 물건 담지 않았을 때 -> 해당 무게의 기존 가격
            # 해당 무게에서, 물건 담았을 때 -> 기존에 w를 담지 않았을 때의 가치에서 +v를 한 것을 비교한다.
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w] + v)

print(dp[n][k])



