def remove_duplicates(numbers: List[int]) -> List[int]:
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

print(remove_duplicates([1, 2, 3, 2, 4]))