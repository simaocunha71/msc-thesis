    def intersection(interval1, interval2):
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        if start > end:
            return "NO"
        length = end - start + 1
        if length < 2:
            return "NO"
        for i in range(2, int(length**0.5) + 1):
            if length % i == 0:
                return "NO"
        return "YES" if length > 1 else "NO"
    # test the function
    print(intersection((1, 2), (2, 3)))  # "NO"
    print(intersection((-1, 1), (0, 4)))  # "NO"
    print(intersection((-3, -1), (-5, 5)))  # "YES"
    print(intersection((0, 1), (2, 3)))  # "NO"
    print(intersection((0, 0), (0, 1)))  # "NO"
    print(intersection((0, 0), (0, 0)))  # "NO"
    print(intersection((1, 1), (1, 1)))  # "NO"

    
    # it is assumed that the intervals are non-empty
    # if there is no intersection, it will return "NO" if the intervals don't intersect, return "NO"
    # it will return "YES" if the length of the intersection is a prime number, otherwise "NO"
    # it will return "NO" if the two intervals are identical, return "NO" if the start of the interval is greater than the end, return "NO" 
    # it will return "YES" if the length of the intersection is 1, return "NO" if the length of the intersection is less than 2, return "NO" 
    # it will return "YES" if the length of the intersection is 2, return "YES" if the length of the intersection is 3, return "NO" 
    # it will return "YES" if the length of the intersection is 5, return "YES" if the length of the intersection is 7, return "NO" 
    # it will return "YES" if the length of the intersection is 11, return "YES" if the length of the intersection is 13,