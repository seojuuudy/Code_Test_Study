# 10*10 미로 생성
arr = [[0] * 10 for i in range(10)]

for i in range(10):
    num = input().split()
    for j in range(10):
        arr[i][j] = int(num[j])

# 개미 시작점 (2,2)
x = 1
y = 1

# 0(갈 수 있음) 1(벽 or 장애물) 2(먹이)
while True :
    # 갈 수 있는 경로 = 9
    if arr[x][y] == 0 :
        arr[x][y] = 9
    # 먹이 있는 곳 = 9    
    elif arr[x][y] == 2 :
        arr[x][y] = 9
        break

    # 1 일 경우 이동 x    
    if(arr[x][y+1] == 1 and arr[x+1][y] == 1) or (x == 9 and y == 9):
        break

    # 오른쪽에 길이 있다면 오른쪽으로 이동
    if arr[x][y+1] != 1 :
        y += 1
     # 아래쪽에 길이 있다면 아래쪽으로 이동    
    elif arr[x+1][y] != 1 :
        x += 1

# 전체출력
for i in range(10) :
    for j in range(10) :
        print(arr[i][j], end = ' ')
    print()


