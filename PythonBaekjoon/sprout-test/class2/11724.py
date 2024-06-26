# 11724. 연결요소의 개수

# 1번째 시도 - 시간초과
# 나의 코드 / 틀린 코드 ing ---------
'''
왜 시간초과...?
방문처리가 제대로 안돼서 중복처리되고있나..?
그래프에 노드 방문처리하는게 시간이 더 걸리나..?
'''

import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
# graph = [[[0] for _ in range(n+1)] for _ in range(n+1)]

cnt = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

def dfs(x):
    #노드 x 방문처리
    graph[x][x] = 1

    #노드 x에 인접한 노드 탐색
    for i in range(1, n+1):
        if graph[x][i]==1 and x != i:
            graph[x][i] = 0
            graph[i][x] = 0
            # graph[i][i] = 1
            dfs(i)



for i in range(1, n+1):
    if graph[i][i] == 0:
        dfs(i)
        cnt += 1


print(cnt)