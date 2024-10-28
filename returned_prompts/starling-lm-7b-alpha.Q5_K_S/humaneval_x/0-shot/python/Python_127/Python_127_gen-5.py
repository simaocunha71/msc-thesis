
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
        return "NO"
    else:
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        length = end - start + 1
        if isPrime(length):
            return "YES"
        else:
            return "NO"



# Test
print(intersection((-3, -1), (-5, 5))) # "YES"
print(intersection((-1, 1), (0, 4))) # "NO"
print(intersection((1, 3), (2, 4))) # "NO"
print(intersection((2, 3), (4, 5))) # "NO"
print(intersection((3, 5), (2, 4))) # "YES"








```