def solution(n, results):
    answer = 0
    INF = int(1e9)
    cost = [[INF] * (n+1) for _ in range(n+1)]
    for i in results:
        cost[i[0]][i[1]] = 1
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==j : cost[i][j] = 0
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if cost[i][j] == INF and cost[j][i] == INF: break
            cnt += 1
        if cnt == n : answer += 1
    return answer