def solution(A, K):
    if(A == []):
        return []
    if(K == 0):
        return A

    count = len(A)
    move_count = K % count

    if(move_count == 0):
        return A
    else:
        first = A[-move_count:]
        last = A[:count-move_count]
    return first + last


# print(solution([3, 8, 9, 7, 6], 0))
# print(solution([3, 8, 9, 7, 6], 1))
# print(solution([3, 8, 9, 7, 6], 2))
# print(solution([3, 8, 9, 7, 6], 3))
# print(solution([3, 8, 9, 7, 6], 4))
# print(solution([3, 8, 9, 7, 6], 5))
# print(solution([3, 8, 9, 7, 6], 6))
