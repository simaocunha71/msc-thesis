    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    if start > end:
        return "NO"
    return "YES" if is_prime(end - start + 1) else "NO"


