def odd_Equivalent(s: str, k: int) -> int:
    def rotate(s: str, k: int) -> str:
        return s[-k:] + s[:-k]

    def count_odd(s: str) -> int:
        return sum(1 for c in s if c == '1')

    n = len(s)
    return sum(count_odd(rotate(s, i)) for i in range(n))