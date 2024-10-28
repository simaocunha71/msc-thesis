
def add(lst):
    # Check for empty list
    if not lst:
        raise ValueError("lst is empty")

    # Check for non-empty list
    if not isinstance(lst, list):
        raise TypeError("lst is not a list")

    # Check for odd indices
    if len(lst) % 2 == 0:
        raise ValueError("lst contains even indices")

    # Check for non-integer elements
    if not all(isinstance(x, int) for x in lst):
        raise TypeError("lst contains non-integer elements")

    # Check for negative elements
    if any(x < 0 for x in lst):
        raise ValueError("lst contains negative elements")

    return sum(x for i, x in enumerate(lst) if i % 2 == 1)

