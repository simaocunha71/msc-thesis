    seen = set()
    result = []

    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result
# Another solution:
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for i, num in enumerate(numbers) if num not in numbers[:i]]


