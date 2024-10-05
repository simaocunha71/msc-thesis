
    def intersection(interval1, interval2):
        if interval1[0] > interval2[1] or interval1[1] < interval2[0]:
            return "NO"
        else:
            start = max(interval1[0], interval2[0])
            end = min(interval1[1], interval2[1])
            return "YES" if (end - start) % 2 != 0 else "NO"



