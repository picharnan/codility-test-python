def solution(A):
    res = 0
    A = sorted(set(A))
    count = len(A)
    has1 = False

    if count == 1:
        if(A[0] <= 0):
            return 1
        else:
            if A[0] == 1:
                return 2
            else:
                return 1

    for i in range(0, count):
        if i + 1 == count:
            res = A[i] + 1
            if has1 == False:
                    res = 1
            break

        if A[i] > 0:
            if A[i] == 1:
                has1 = True

            if A[i] > 1 and has1 == False:
                return 1

            if A[i]+1 != A[i+1]:
                res = A[i]+1
                if has1 == False:
                    res = 1
                break
        else:
            res = A[i]

    if res <= 0:
        res = 1

    return res

# print(solution( [-4, 1, 3, 6, 4, 1, 2]))
print(solution( [-1, -3]))
# print(solution( [1, 2, 3]))