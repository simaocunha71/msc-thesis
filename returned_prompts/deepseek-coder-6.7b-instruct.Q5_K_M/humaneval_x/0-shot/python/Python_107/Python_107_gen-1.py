
def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]: # check if palindrome
            if i % 2 == 0:  # check if even
                even_count += 1
            else:  # else it's odd
                odd_count += 1
    return even_count, odd_count

print(even_odd_palindrome(3))  # Expected Output: (1, 2)
print(even_odd_palindrome(12))  # Expected Output: (4, 6)

# Solution:
# The function first initializes two counters, one for even palindromes and one for odd palindromes.
# Then it loops over all integers from 1 up to n. For each integer i, it first checks if i is a palindrome.
# This is done by converting i to a string and comparing it with its reverse (str(i)[::-1]). If they are equal, i is a palindrome.
# If i is a palindrome, it then checks if it is even by checking if the remainder of i divided by 2 is 0 (i % 2 == 0).
# If i is even, it increments the even counter. Otherwise, it increments the odd counter.
# Finally, it returns a tuple with the counters.
# This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.
# It also correctly counts the number of even and odd palindromes within the range.

# Note:
# The function uses Python's slicing syntax to create the reversed string. The syntax str(i)[::-1] means "create a new string from the characters in str(i) in reverse order".
# In this case, str(i) is the string representation of i, and [::-1] tells Python to start at the end of the string and end at position 0, stepping backwards by 1 character at a time.
# This effectively reverses the string.
<jupyter_output>
(