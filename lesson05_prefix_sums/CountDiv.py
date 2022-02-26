def solution(A, B, K):
    res = 0

    res = (B / K) - (A / K) 

    if A % K == 0 :
        res += 1

    return int(res)

# print(solution(2, 2, 2))
# print(solution(0, 14, 2))
print(solution(0, 14, 3))
# print(solution(6, 11, 2))
# print(solution(6, 11, 7))
# print(solution(6, 11, 3))
# print(solution(1,1,11))
# print(solution(0, 10 , 3))
