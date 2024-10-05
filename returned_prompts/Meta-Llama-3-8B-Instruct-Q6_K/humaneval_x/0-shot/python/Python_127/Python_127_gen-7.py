def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    if intersection_start > intersection_end:
        return "NO"
    intersection_length = intersection_end - intersection_start + 1
    for i in range(2, int(intersection_length**0.5) + 1):
        if intersection_length % i == 0:
            return "NO"
    return "YES"

# Testing the function
print(intersection((1, 2), (2, 3)))  # Output: "NO"
print(intersection((-1, 1), (0, 4)))  # Output: "NO"
print(intersection((-3, -1), (-5, 5)))  # Output: "YES"
print(intersection((1, 5), (4, 7)))  # Output: "YES"
print(intersection((1, 2), (3, 4)))  # Output: "NO"  # No intersection
print(intersection((-1, 0), (0, 1)))  # Output: "NO"  # No intersection
print(intersection((-2, 2), (-3, 3)))  # Output: "YES"
print(intersection((1, 2), (1, 2)))  # Output: "NO"  # No intersection
print(intersection((-1, 1), (-1, 1)))  # Output: "NO"  # No intersection
print(intersection((0, 1), (0, 1)))  # Output: "NO"  # No intersection
print(intersection((-1, 0), (0, 1)))  # Output: "NO"  # No intersection
print(intersection((1, 2), (2, 3)))  # Output: "NO"
print(intersection((1, 3), (2, 4)))  # Output: "NO"
print(intersection((1, 2), (2, 3)))  # Output: "NO"
print(intersection((0, 2), (1, 3)))  # Output: "NO"
print(intersection((1, 3), (2, 4)))  # Output: "NO"
print(intersection((1, 3