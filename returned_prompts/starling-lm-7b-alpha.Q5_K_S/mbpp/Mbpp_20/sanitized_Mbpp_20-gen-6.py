def is_woodall(n):
    # Convert the number to a string, then rearrange its digits
    digits = map(int, list(str(n)))
    digits.sort()
    # Reverse the digits and convert them back to an integer
    n = int(''.join(map(str, digits)))
    # Check if the rearranged number is a palindrome
    return str(n) == ''.join(map(str, reversed(list(str(n)))))