from bisect import bisect_left, bisect_right

def count_index(li, left_value, right_value):
    left_index = bisect_left(li, left_value)
    right_index = bisect_right(li, right_value)
    return right_index - left_index
    
def solution(words, queries):
    answer = []
    arr_len = [[] for _ in range(10001)]
    arr_reverse = [[] for _ in range(10001)]
    
    for i in words:
        slen = len(i)
        arr_len[slen].append(i)
        arr_reverse[slen].append(i[::-1])
    
    for i in range(10001):
        arr_len[i].sort()
        arr_reverse[i].sort()
    
    for query in queries :
        if query[0] != '?':
            cnt = count_index(arr_len[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
        else :
            cnt = count_index(arr_reverse[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
        answer.append(cnt)
    return answer