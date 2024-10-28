```
def even_odd_palindrome(n):
    even = 0
    odd = 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```



This function works by iterating over the range from 1 to n (inclusive), and for each number, it checks if it is a palindrome by comparing the string representation of the number with its reverse. If it is a palindrome, it checks if the number is even or odd. If the number is even, it increments the even count; otherwise, it increments the odd count. Finally, it returns a tuple containing the counts of even and odd palindromes. 

The time complexity of this function is O(n) because it needs to iterate over the range from 1 to n. The space complexity is O(1) because it only uses a constant amount of space to store the counts of even and odd palindromes. 

Please note that this function assumes that the input n is a positive integer. If n can be 0, you may want to add a check at the beginning of the function to handle this case. 

Also, the function returns a tuple with the counts of even and odd palindromes in the order (even, odd). If you want to return the counts in the order (odd, even), you can simply swap the values of the even and odd variables at the end of the function. 