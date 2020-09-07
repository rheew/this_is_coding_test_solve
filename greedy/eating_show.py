import heapq

def solution(food_times, k):
    if sum(food_times) <= k : return -1
    answer = 0
    h = []
    for ind, i in enumerate(food_times):
        heapq.heappush(h, (i, ind + 1))
    
    pre = 0
    sum_time = 0
    
    while h :
        cur_time = h[0][0]
        if sum_time + (cur_time - pre) *len(h) > k:
            break
        sum_time += (cur_time - pre) * len(h)
        heapq.heappop(h)
        pre = cur_time
    
    result = sorted(h, key=lambda x:x[1])
    answer = result[(k - sum_time) % len(h)][1]
    return answer