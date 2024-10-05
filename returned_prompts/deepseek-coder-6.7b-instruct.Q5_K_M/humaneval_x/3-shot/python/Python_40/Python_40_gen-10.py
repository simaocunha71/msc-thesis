    l.sort()
    for i in range(len(l) - 2):
        start = i + 1
        end = len(l) - 1
        while start < end:
            if l[i] + l[start] + l[end] < 0:
                start += 1
            elif l[i] + l[start] + l[end] > 0:
                end -= 1
            else:
                return True
    return False


