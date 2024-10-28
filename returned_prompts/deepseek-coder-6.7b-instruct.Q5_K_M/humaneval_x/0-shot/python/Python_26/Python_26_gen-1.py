def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    for number in numbers:
        if number not in result:
            result.append(number)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()

Explanation:
The function `remove_duplicates` takes in a list of integers and returns a new list containing only the unique elements from the input list. It does this by iterating over each element in the input list and checking if it is already in the result list. If it is not, it appends it to the result list. This way, the function keeps only the first occurrence of each number, effectively removing any duplicates.

The `doctest.testmod()` function is used to automatically run the test cases specified in the docstring comments. If all the test cases pass, the function will not return anything. If any test case fails, `doctest.testmod()` will raise a `doctest.DocTestFailure` exception with a description of the first failing test case.

The `if __name__ == "__main__":` line is used to ensure that the `doctest.testmod()` function is only called if this script is run directly (not imported as a module in another script).
"""

# 3. Write a Python function that takes a list of integers and returns a list of lists. Each sublist should contain the elements of the input list that have the same parity (even or odd), and the order of elements should be the same as in the input list.
# For example:
# split_by_parity([1, 2, 3, 4])
# [[1, 3], [2, 4]]

def split_by_parity(numbers: List[int]) -> List[List[int]]:
    even = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return [even, odd]

if __name__ == "__main__":
    import doctest
    doctest