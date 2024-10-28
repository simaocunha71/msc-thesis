
def intersection(interval1, interval2):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    if start <= end:
        return "NO"
    else:
        if start == end:
            if start % 2 == 0:
                return "NO"
            else:
                return "YES"
        else:
            return "YES"


    # Test case 1:
    print(intersection((-1, 1), (0, 4)))
    # Output: NO

    # Test case 2:
    print(intersection((-3, -1), (-5, 5)))
    # Output: YES

    # Test case 3:
    print(intersection((1, 2), (2, 3)))
    # Output: NO

    # Test case 4:
    print(intersection((-1, 1), (-2, 2)))
    # Output: YES

    # Test case 5:
    print(intersection((-1, 1), (-2, 1)))
    # Output: YES

    # Test case 6:
    print(intersection((-1, 1), (-2, 0)))
    # Output: NO

    # Test case 7:
    print(intersection((-1, 1), (-2, 0.5)))
    # Output: NO

    # Test case 8:
    print(intersection((-1, 1), (-2, 0.6)))
    # Output: YES

    # Test case 9:
    print(intersection((-1, 1), (-2, 1.5)))
    # Output: NO

    # Test case 10:
    print(intersection((-1, 1), (-2, 1.6)))
    # Output: YES

    # Test case 11:
    print(intersection((-1, 1), (-2, 1.7)))
    # Output: YES

    # Test case 12:
    print(intersection((-1, 1),