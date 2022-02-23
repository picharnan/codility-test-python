def solution(A):
    n = len(A)
    sum = 0
    for i in A:
        sum += i
    correct_n = n + 1
    correct_sum = (correct_n * (correct_n+1)) / 2

    return int(correct_sum) - int(sum)


print(solution([2, 3, 1, 5]))
print(solution([2, 3, 1, 5, 4, 7, 8]))
