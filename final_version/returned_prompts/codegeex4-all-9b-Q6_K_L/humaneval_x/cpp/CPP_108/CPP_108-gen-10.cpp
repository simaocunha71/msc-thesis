def count_nums(n):
    sum = 0
    count = 0
    for i in n:
        sum = 0
        if i < 0:
            i = abs(i)
            while i > 0:
                sum += i % 10
                i = i // 10
            if sum < 0:
                count += 1
        else:
            while i > 0:
                sum += i % 10
                i = i // 10
            if sum > 0:
                count += 1
    return count
