def count_samepair(a, b, c):
    count = 0
    for i in range(len(a)):
        if a[i] == b[i] == c[i]:
            count += 1
    return count