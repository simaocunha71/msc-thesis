def next_smallest_palindrome(n):
    # Convert the integer to a string
    s = str(n)
    
    # Check if the string is already a palindrome
    if s == s[::-1]:
        return -1
    
    # Find the next smaller palindrome
    while True:
        # Generate the next smaller palindrome
        s = s[:-1] + s[-2::-1]
        
        # Convert the modified string back to an integer
        try:
            n = int(s)
            break
        except ValueError:
            pass
    
    return n