def solution(X, A):

    leafs = set()
    for i in range(0,len(A)):
        leafs.add(A[i])
        if(len(leafs) == X):
            return i

    return -1


print(solution(5, [1,3,1,4,2,3,5,4]))