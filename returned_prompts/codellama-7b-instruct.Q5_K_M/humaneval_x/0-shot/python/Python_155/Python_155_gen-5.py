
def even_odd_count(num):
    count1 = 0
    count2 = 0
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            count1 += 1
        else:
            count2 += 1
    if num < 0:
        return (count2, count1)
    else:
        return (count1, count2)
