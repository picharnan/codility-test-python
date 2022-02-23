def solution(A):
    if(len(A) == 1 and A[0] != 1):
        return 0

    if(len(A) == 1 and A[0] == 1):
        return 1
    
    A.sort()

    if(A[0] != 1):
        return 0

    for i in range(0, len(A) - 1):
        if((A[i]+1) != A[i+1]):
            return 0

    return 1

print(solution([2]))
print(solution([4,1,3,2]))