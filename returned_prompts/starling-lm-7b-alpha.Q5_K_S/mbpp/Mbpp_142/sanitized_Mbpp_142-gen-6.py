def count_samepair(a, b, c):
    if len(a) != len(b) or len(b) != len(c):
        return 0
    else:
        count = 0
        for i in range(len(a)):
            if a[i] == b[i] == c[i]:
                count += 1
        return count