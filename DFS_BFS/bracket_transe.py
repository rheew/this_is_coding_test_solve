from collections import deque

def reverse(s):
    result = ''
    for i in s:
        if i == '(' : result += ')'
        else : result += '('
    return result

def trans(w):
    if w == '' : return ''
    ans = ''
    uIndex = findBalance(w)
    u, v = w[:uIndex+1], w[uIndex+1:]
    if isRightString(u) : ans = u + trans(v)
    else :
        u = u[1:-1]
        u = reverse(u)
        ans = '(' + trans(v) + ')' + u
    return ans

def isRightString(s):
    d = deque()
    for i in s:
        if i =='(':
            d.append(i)
        elif not d : return False
        else : d.popleft()
        
    return True

def findBalance(s):
    left = 0
    right = 0
    for i in range(len(s)):
        if s[i] == '(': left += 1
        else : right += 1
        if left == right : return i

def solution(p):
    answer = trans(p)
    return answer