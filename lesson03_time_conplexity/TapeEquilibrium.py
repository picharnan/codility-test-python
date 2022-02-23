def solution(A):

    count_element = len(A)
    min_diff = 0
    sum_all = 0

    for i in A:
        sum_all = sum_all + i

    left = 0
    for i in range(1, count_element):

        left = left + A[i-1]
        right = sum_all - left

        if(i == 1):
            diff = left - right
            if(diff < 0):
                diff = diff * -1
            min_diff = diff

        if(i > 1):
            diff = left - right
            if(diff < 0):
                diff = diff * -1
            if(diff < min_diff):
                min_diff = diff

    return min_diff


# print(solution([1,2,3,4,5,6,7,8]))
print(solution([3, 1, 2, 4, 3]))
