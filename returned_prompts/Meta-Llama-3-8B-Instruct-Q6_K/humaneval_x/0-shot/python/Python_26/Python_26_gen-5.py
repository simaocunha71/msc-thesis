from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    unique_numbers = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            unique_numbers.append(num)
    return unique_numbers
    # or, with a dictionary
    # return [num for num in numbers if (num, None) not in seen]
    # or, with a list comprehension
    # return [num for num in set(numbers)]


# test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5, 5, 5]))  # Output: [1, 2, 3, 4, 5]
print(remove_duplicates([1, 1, 1, 1, 1]))  # Output: [1]  # only 1 in the list
print(remove_duplicates([]))  # Output: []  # empty list
print(remove_duplicates([1]))  # Output: [1]  # single element, no duplicates
print(remove_duplicates([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]  # no duplicates
print(remove_duplicates([1, 2, 3, 3, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]  # duplicates removed
print(remove_duplicates([1, 2, 3, 4, 5, 5, 5, 5]))  # Output: [1, 2, 3, 4, 5]  # duplicates removed
print(remove_duplicates([1, 2, 3, 4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]  # no duplicates
print(remove_duplicates([1, 2, 3, 4, 5, 6, 7]))  # Output: [1, 2, 3, 4, 5, 6, 7]  # no duplicates
print(remove_duplicates([1, 2, 