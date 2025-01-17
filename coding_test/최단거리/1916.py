import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input()) #도시의 갯수
M = int(input()) #버스의 갯수
graph = [[] for i in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, ( cost , i[0]))

start1 , end1 = map(int, input().split())

djikstra(start1)

print(distance[end1])
