    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    if end >= start:
        return "NO"

    length = end - start

    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return "NO"

    return "YES"


