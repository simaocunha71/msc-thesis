from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    return [n for n, c in Counter(numbers).items() if c == 1]