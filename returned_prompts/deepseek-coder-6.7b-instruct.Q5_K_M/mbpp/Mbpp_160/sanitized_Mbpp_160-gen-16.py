def find_solution(a, b, n):
    results = [(x, (n - a * x) // b) for x in range(n // a + 1) if (a * x) % b == n % b]
    return results[0] if results else None