```
def next_smallest_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n

def is_palindrome(n):
    return str(n) == str(n)[::-1]
```    
Explanation:
The function `next_smallest_palindrome` takes an integer `n` as input, increments it by 1, and then checks if the new number is a palindrome. If not, it increments it again and checks again, until it finds the smallest palindrome. The function `is_palindrome` checks if a number is a palindrome by comparing it with its reverse. The unit test `assert next_smallest_palindrome(99)==101` ensures that the function returns the correct result. 

This solution assumes that the input integer is a positive integer. If the input can be any integer, the function should handle negative integers and zero separately. For example, `next_smallest_palindrome(-1)` should return `0`, and `next_smallest_palindrome(0)` should return `1`. 

Also, the function does not handle the case where the input is a palindrome itself. If the input is a palindrome, the function should return the next smallest palindrome. For example, `next_smallest_palindrome(121)` should return `131`. 

The time complexity of this solution is O(log n) because the function increments the number by 1 in each iteration, and the number of digits in the number grows logarithmically with the value of the number. The space complexity is O(1) because the function only uses a constant amount of space to store the number and the flag. 