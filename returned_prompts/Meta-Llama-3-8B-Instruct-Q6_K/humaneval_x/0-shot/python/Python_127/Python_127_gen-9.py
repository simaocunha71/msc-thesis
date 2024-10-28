```
def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    
    # check if intervals intersect
    if start2 > end1 or start1 > end2:
        return "NO"
    
    # calculate the length of intersection
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    intersection_length = intersection_end - intersection_start
    
    # check if the length of intersection is prime
    if intersection_length < 2:
        return "NO"
    for i in range(2, int(intersection_length ** 0.5) + 1):
        if intersection_length % i == 0:
            return "NO"
    return "YES"
```


Explanation:
The function takes two intervals as input, checks if they intersect, calculates the length of the intersection, and checks if the length is a prime number. If the intervals don't intersect, the function returns "NO". Otherwise, it returns "YES" if the length is prime, and "NO" otherwise.

The function first checks if the intervals intersect by comparing their start and end points. If the intervals don't intersect, the function returns "NO".

Then, the function calculates the length of the intersection by finding the maximum of the start points and the minimum of the end points.

Next, the function checks if the length of the intersection is prime. It first checks if the length is less than 2, in which case it's not prime, and returns "NO". Then, it iterates from 2 to the square root of the length, checking if the length is divisible by any of these numbers. If it is, the length is not prime, and the function returns "NO". If the length is prime, the function returns "YES".

Note that the function uses the fact that a composite number (i.e., a non-prime number) must have a factor less than or equal to its square root. This allows us to efficiently check if a number is prime by only considering factors up to its square root.