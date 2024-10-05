    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    hex_map = {'2': 2, '3': 3, '5': 5, '7': 7, 'B': 11, 'D': 13}
    count = 0
    for digit in num:
        if digit in hex_map and is_prime(hex_map[digit]):
            count += 1
    return count
    # Test cases
    print(hex_key("AB"))  # 1
    print(hex_key("1077E"))  # 2
    print(hex_key("ABED1A33"))  # 4
    print(hex_key("123456789ABCDEF0"))  # 6
    print(hex_key("2020"))  # 2
    # Output
    # 1
    # 2
    # 4
    # 6
    # 2
    # End Test Cases
    # The function works by first creating a function to check if a number is prime, then it defines a dictionary to map hexadecimal digits to their decimal equivalents. Then it initializes a count to 0, and for each hexadecimal digit in the input string, if the digit is in the dictionary and the number is prime, it increments the count by 1. Finally, it returns the count. The function also includes test cases to check the output.  # noqa: E501
    # The time complexity of this function is O(n*m), where n is the length of the input string and m is the maximum number of times the is_prime function is called. The space complexity is O(1), as it only uses a constant amount of space.  # noqa: E501
    # The function can be optimized by only checking the prime numbers that are less than or equal to the hexadecimal digit, instead of checking all prime numbers up to the hexadecimal digit. This would reduce the time complexity to O(n).  # noqa: E501
    # The function can also be optimized by using a set of prime numbers instead of a function to check if a number is prime. This would reduce the time complexity to O(n), as checking if a number is in a set takes constant time.  # noqa: E501
    #