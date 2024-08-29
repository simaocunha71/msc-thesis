def count_samepair(a,b,c):
    count = 0
    for i in range(len(a)):
        if a[i] == b[i] == c[i]:
            count += 1
    return count

print(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]))


# 2.
