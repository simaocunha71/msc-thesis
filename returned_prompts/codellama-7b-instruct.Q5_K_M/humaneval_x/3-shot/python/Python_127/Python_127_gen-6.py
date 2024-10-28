    def intersection_len(start1, end1, start2, end2):
        if start1 <= start2:
            start = start2
        else:
            start = start1

        if end1 <= end2:
            end = end1
        else:
            end = end2

        if start > end:
            return 0

        return end - start

    if intersection_len(interval1[0], interval1[1], interval2[0], interval2[1]) > 0:
        if intersection_len(interval1[0], interval1[1], interval2[0], interval2[1]) == 1:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


