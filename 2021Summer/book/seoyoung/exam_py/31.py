'''
## 금광

### 1. 문제
nXm 크기의 금광. 금공은 1X1 크기.
채굴자는 첫 번째 열부터 출발
맨 처음에는 첫 번째 열의 어느 행에서든 출발 가능
m번에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래 3중 하나의 위치로 이동
채굴자가 얻을 수 있는 금의 최대 크기는?

### 2. 다이나믹 프로그래밍 리뷰
- 한 번 해결된 부분 문제의 정답을 메모리에 기록하여, 한 번 계산한 답은 다시 계산하지 않도록 하는 문제 해결 기법
- 인접한 항들 사이의 관계식인 점화식을 그대로 코드로 옮겨서 구현 가능.
- 탑다운 방식 : 재귀 함수 이용. 큰 문제를 해결하기 위해 작은 문제를 호출
- 보텀업 방식 : 단순히 반복문을 이용해 작은 문제를 먼저 해결, 해결된 작은 문제를 모아 큰 문제를 해결

### 3. 문제 해결 방향
- 계산을 다 해서 저장한다.
- 금광의 모든 위치에 대하여, 1) 왼쪽 위, 2) 왼쪽 아래, 3) 왼쪽에서 오는 3가지 경우 중 가장 많은 금을 가지고 있는 경우를 저장한다.
- 2차원 테이블을 이용한다.

'''

# 태스트 케이스
T = int(input())

# 매장된 금의 개수
for _ in range(T):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m]) # 테스트 케이스가 한줄로 입력되므로 m 단위로 슬라이싱해서 넣는다.
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

        result = 0
        for i in range(n):
            result = max(result, dp[i][m-1])

        print(result)