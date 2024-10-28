def next_smallest_palindrome(n):
    # Convert the number to a string
    str_n = str(n)

    # Check if the number is already a palindrome
    if str_n == str_n[::-1]:
        # If it is, find the next smallest palindrome
        while str_n == str_n[::-1]:
            n -= 1
            str_n = str(n)
    else:
        # If it is not, find the next smallest palindrome
        while str_n != str_n[::-1]:
            n -= 1
            str_n = str(n)

    return int(str_n)