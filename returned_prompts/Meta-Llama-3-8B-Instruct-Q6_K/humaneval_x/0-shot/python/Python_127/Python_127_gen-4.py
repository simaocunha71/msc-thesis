```
def intersection(interval1, interval2):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    if start > end:
        return "NO"
    length = end - start + 1
    if length <= 1:
        return "NO"
    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
            return "NO"
    return "YES"
```


This function first calculates the start and end points of the intersection of the two intervals. If the intersection is empty (i.e., the start point is greater than the end point), it returns "NO". It then calculates the length of the intersection. If the length is 1 or less, it returns "NO". Finally, it checks if the length is a prime number by checking divisibility from 2 to the square root of the length. If the length is a prime number, it returns "YES", otherwise it returns "NO".