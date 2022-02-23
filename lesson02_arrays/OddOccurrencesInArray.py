def solution(A):
    if(len(A) == 1):
        return A[0]
    A.sort()

    for idx in range(0, len(A), 2):
        if(idx + 1 >= len(A)):
            return A[idx]

        if(A[idx] != A[idx+1]):
            return A[idx]

    return 0


# print(solution([]))
# print(solution([7]))
# print(solution([9, 3, 9, 3, 9, 7, 9]))
print(solution([1, 9, 3, 9, 3, 9, 7, 9, 7, 10, 10]))
