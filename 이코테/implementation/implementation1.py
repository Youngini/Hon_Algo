# 상하좌우
import sys
input = sys.stdin.readline

N = int(input())
plans = input().split()

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dir = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(4):
        if plan == dir[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue

    x , y = nx, ny

print(x, y)
        