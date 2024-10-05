
    distinct_chars = set()
    for char in string:
        if char.isalpha():
            distinct_chars.add(char.lower())
    return len(distinct_chars)


# Testing
print(count_distinct_characters('xyzXYZ'))  # Expected: 3
print(count_distinct_characters('Jerry'))  # Expected: 4
print(count_distinct_characters('123'))  # Expected: 0
print(count_distinct_characters('Hello, World!'))  # Expected: 8
print(count_distinct_characters(''))  # Expected: 0










def solution(arr, limit):
    # Sort the array
    arr.sort()
    # Initialize the result
    result = arr[0]
    for i in range(len(arr)):
        if arr[i] <= limit:
            result += arr[i]
    return result



def main():
    arr = [int(x) for x in input().split()]
    limit = int(input())
    result = solution(arr, limit)
    print(result)

if __name__ == '__main__':
    main()



# Given an array of integers and a limit, find the maximum sum of the subarray such that the maximum value of the subarray is less than or equal to the limit
# You need to implement the solution


def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    distinct_chars = set()
    for char in string:
        if char.isalpha():
            distinct_chars.add(char.lower())
    return len(distinct_chars)


# Testing
print(count_distinct_characters('xyzXYZ'))  # Expected: 3
print(count_distinct_char