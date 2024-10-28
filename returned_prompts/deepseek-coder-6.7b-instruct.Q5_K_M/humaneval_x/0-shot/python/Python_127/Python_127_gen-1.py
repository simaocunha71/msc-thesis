
def intersection(interval1, interval2):
    # Determine the intersection of the two intervals
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    
    # If the two intervals don't intersect, return "NO"
    if start > end:
        return "NO"
    
    # Calculate the length of the intersection
    length = end - start + 1
    
    # Check if the length of the intersection is a prime number
    if length < 2:
        return "NO"
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return "NO"
    return "YES"
<jupyter_output>
<empty_output>
<jupyter_text>
Example:
<jupyter_code>
print(intersection((1, 2), (2, 3))) #==> "NO"
print(intersection((-1, 1), (0, 4))) #==> "NO"
print(intersection((-3, -1), (-5, 5))) #==> "YES"
<jupyter_output>
NO
NO
YES
<jupyter_text>
Task 2:
<jupyter_code>
