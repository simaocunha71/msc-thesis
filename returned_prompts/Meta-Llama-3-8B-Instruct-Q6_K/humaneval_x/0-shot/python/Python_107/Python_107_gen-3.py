```
def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)
```



This function iterates over the range from 1 to n (inclusive) and checks each number to see if it's a palindrome by comparing the string representation of the number to its reverse. If the number is a palindrome, it then checks whether the number is even or odd. If the number is even, it increments the even_count, otherwise it increments the odd_count. Finally, it returns a tuple containing the even_count and odd_count.

Here's how you can use the function:
```
print(even_odd_palindrome(3))  # Output: (1, 2)
print(even_odd_palindrome(12))  # Output: (4, 6)
```



This function is efficient because it only iterates over the range from 1 to n once, and it uses a constant amount of extra space to store the counts. The time complexity is O(n) and the space complexity is O(1).