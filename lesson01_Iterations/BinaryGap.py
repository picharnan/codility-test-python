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

print(solution(0))