
def max_run_uppercase(s: str) -> int:
    return len(max(zip(*[s[i:].split() for i in range(len(s))])))


