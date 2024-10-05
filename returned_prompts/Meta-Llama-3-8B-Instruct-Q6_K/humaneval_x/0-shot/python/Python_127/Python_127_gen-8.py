def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    
    if intersection_start > intersection_end:
        return "NO"
    
    intersection_length = intersection_end - intersection_start + 1
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"






# test cases:
print(intersection((1, 2), (2, 3)))  # "NO"
print(intersection((-1, 1), (0, 4)))  # "NO"
print(intersection((-3, -1), (-5, 5)))  # "YES"
print(intersection((1, 4), (2, 6)))  # "YES"
print(intersection((-2, 2), (1, 3)))  # "NO"







# test cases with intervals that don't intersect:
print(intersection((1, 2), (3, 4)))  # "NO"
print(intersection((-1, 1), (-3, -2)))  # "NO"
print(intersection((0, 1), (2, 3)))  # "NO"
print(intersection((-2, -1), (0, 1)))  # "NO"
print(intersection((1, 2), (4, 5)))  # "NO"







# test cases with intervals that have the same start or end:
print(intersection((1, 2), (1, 3)))  # "NO"
print(intersection((-1, 1), (-1, 2)))  # "NO"
print(intersection((1, 2), (2, 2)))  # "NO"
print(intersection((-2, 2), (-2, 2)))  # "NO"
print(intersection((1, 1), (1, 1)))  # "NO"





# test cases with intervals that have the same start and end:
print(intersection((1, 1), (1, 1))) 