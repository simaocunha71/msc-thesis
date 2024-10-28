
def rounded_avg(n, m):
    if n > m:
        return -1
    sum = 0
    for i in range(n, m+1):
        sum += i
    return "0b" + str(round(sum/len(range(n, m+1))))
