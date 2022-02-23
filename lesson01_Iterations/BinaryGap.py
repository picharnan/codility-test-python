def solution(N):
    count_gap = 0
    count_maximum_gap = 0
    binstr = "{0:b}".format(N)

    for i in binstr:
        if(i == '1'):
            if(count_maximum_gap < count_gap):
                count_maximum_gap = count_gap
            count_gap = 0
        if(i == '0'):
            count_gap = count_gap + 1

    return count_maximum_gap


print(solution(1041))       # 5
print(solution(10))         # 1
print(solution(342))        # 1
print(solution(20))         # 1
print(solution(529))        # 1
