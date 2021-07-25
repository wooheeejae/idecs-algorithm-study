### 계수 정렬(count sort)
## 특정한 조건이 부합할 때만 사용 가능, 그러나 매우 빠름
## 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능
## 모든 범위를 다 담을 수 있는 크기의 리스트(배열)를 선언
## 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다.
## 몇 번 나왔는지 해당 인덱스의 값을 1씩 추가, 그 수만큼 인덱스 출력

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')  # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

## 계수 정렬의 시간 복잡도는 O(N+K). 데이터의 범위만 한정되어 있다면 효과적으로 사용 가능. 항상 빠르게 동작
## 계수 정렬은 때에 따라서 심각한 비효율성을 초래 가능. 최소값과 최대값이 크게 차이 나면 별로.. 동일한 값을 가지는 데이터가 여러 개 등장할 때 적합.
## 데이터의 특성을 파악하기 어렵다면 퀵 정렬을 이용하는 것이 유리
## 계수 정렬의 공간 복잡도는 O(N+K)

