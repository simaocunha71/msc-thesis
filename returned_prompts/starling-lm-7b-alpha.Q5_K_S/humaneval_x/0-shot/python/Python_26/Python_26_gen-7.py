    seen = set()  # a set is a collection of unique elements
    result = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result





def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    seen = set()  # a set is a collection of unique elements
    result = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result



# Example usage:
def main():
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    print(result)

if __name__ == "__main__":
    main()















































































































































































































































