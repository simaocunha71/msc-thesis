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







# Testing the function
print(intersection((1, 2), (2, 3)))  # Should print "NO"
print(intersection((-1, 1), (0, 4)))  # Should print "NO"
print(intersection((-3, -1), (-5, 5)))  # Should print "YES"
print(intersection((1, 3), (2, 4)))  # Should print "NO"







# Explanation:
The function first calculates the start and end of the intersection by taking the maximum of the start of the intervals and the minimum of the end of the intervals. If the start of the intersection is greater than the end, it means the intervals don't intersect, so the function returns "NO".

Then, the function calculates the length of the intersection by subtracting the start from the end and adding 1 (since the interval is closed).

The function then checks if the length of the intersection is a prime number using a helper function `is_prime`. If the length is a prime number, the function returns "YES", otherwise it returns "NO".