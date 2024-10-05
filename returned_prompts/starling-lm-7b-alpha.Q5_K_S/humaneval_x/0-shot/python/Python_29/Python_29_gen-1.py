
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
print(filter_by_prefix([], 'a'))  # Should return []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Should return ['abc',