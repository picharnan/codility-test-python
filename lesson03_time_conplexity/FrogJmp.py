import math

def solution(X,Y,D):
    step = math.ceil((Y-X) / D)
    return step


print(solution(10,85,30))