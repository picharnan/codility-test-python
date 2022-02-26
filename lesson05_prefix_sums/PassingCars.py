def solution(A):
    res = 0
    count0 = 0
    for i in A:
        if i == 0:
            count0 += 1
        if i == 1:
            res = res + count0

    if res > 1000000000:
        res = -1

    return res

print(solution([0,1,0,1,1]))