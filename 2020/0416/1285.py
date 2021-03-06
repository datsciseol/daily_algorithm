import sys
import copy
N = int(input())
MAX = 500
graph = [list(input().rstrip()) for _ in range(N)]
def flip(graph, row):
    for col in range(N):
        if graph[row][col] == "H":
            graph[row][col] = "T"
        else:
            graph[row][col] = "H"
def count(graph, col):
    HEAD = 0
    TAIL = 0
    for row in range(N):
        if graph[row][col] == "H":
            HEAD += 1
        else:
            TAIL += 1
    return (HEAD, TAIL)
ans = MAX
for iter in range(1 << N):
    temp = 0
    base = copy.deepcopy(graph)
    for jter in range(N):
        if iter & (1 << jter):
            flip(base, jter)
    for kter in range(N):
        HEAD, TAIL = count(base, kter)
        if HEAD > TAIL:
            temp += TAIL
        else:
            temp += HEAD
    if ans > temp:
        ans = temp
print(ans)

    
