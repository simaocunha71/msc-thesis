    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for idx in range(2, int(n ** 0.5) + 1):
            if n % idx == 0:
                return False
        return True

    def length(start: int, end: int) -> int:
        return end - start + 1

    if length(interval1[0], interval1[1]) < length(interval2[0], interval2[1]):
        start, end = interval2
        interval2 = interval1
        interval1 = (start, end)

    end1, start2 = interval1
    start, end2 = interval2

    length_intersection = max(end1, end2) - min(start1, start2) + 1
    if length_intersection < 0:
        return "NO"
    if is_prime(length_intersection):
        return "YES"
    return "NO"


