def divisible_by_digits(startnum, endnum):
    """
    >>> divisible_by_digits(1,22)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    """
    # your code goes here
    result = []
    for i in range(startnum, endnum + 1):
        if all(i % j == 0 for j in str(i)):
            result.append(i)
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()









"""
To solve this problem, we need to iterate through the range from startnum to endnum, and for each number, check if it is divisible by all its digits. We can do this by converting the number to a string and iterating through each digit in the string, checking if the number is divisible by each digit. If it is divisible by all its digits, we add it to the result list. Finally, we return the result list.

The time complexity of this solution is O(n), where n is the number of numbers in the range from startnum to endnum. The space complexity is O(1), as we are only using a fixed-size result list to store the numbers that are divisible by all their digits.
"""

"""
Explanation:

To solve this problem, we need to iterate through the range from startnum to endnum, and for each number, check if it is divisible by all its digits. We can do this by converting the number to a string and iterating through each digit in the string, checking if the number is divisible by each digit. If it is divisible by all its digits, we add it to the result list. Finally, we return the result list.

The time complexity of this solution is O(n), where n is the number of numbers in the range from startnum to endnum. The space complexity is O(1), as we are only using a fixed-size result list to store the numbers that are divisible by all their digits.
