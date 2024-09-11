def next_smallest_palindrome(n):
    if n % 10 == 9:
        n += 1
        while not is_palindrome(n):
            n += 1
    else:
        n = n + 10 - (n % 10)
        while not is_palindrome(n):
            n += 1
    return n
def is_palindrome(n):
    return str(n) == str(n)[::-1]  # converting to string and checking if it's equal to its reverse.  # Python's slice notation is used to reverse the string.  # If they are equal, the number is a palindrome.  # If not, it's not.  # This function works for any type of number.  # It will check if the number is equal to its reverse as a string.  # If they are equal, the number is a palindrome.  # If not, it's not.  # This function works for any type of number.  # It will check if the number is equal to its reverse as a string.  # If they are equal, the number is a palindrome.  # If not, it's not.  # This function works for any type of number.  # It will check if the number is equal to its reverse as a string.  # If they are equal, the number is a palindrome.  # If not, it's not.  # This function works for any type of number.  # It will check if the number is equal to its reverse as a string.  # If they are equal, the number is a palindrome.  # If not, it's not.  # This function works for any type of number.  # It will check if the number is equal to its reverse as a string.  # If they are equal, the number is a palindrome.  # If not, it's not.  # This function works for any type of number.  # It will check if the number is equal to its reverse as a string.  # If they are equal, the number is a palindrome.  # If not, it's not.  # This function works for any type of number.  # It will check if the number is equal to its reverse as a string.  # If they are equal, the number is a palindrome.  # If not, it's not.  # This function works for any type of number.  # It will check if the number is equal