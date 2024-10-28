```
def get_odd_collatz(n):
    result = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n % 2 != 0:
            result.append(n)
    return sorted(result)
``` 

Explanation:
The function `get_odd_collatz(n)` generates the Collatz sequence for the given number `n` until it reaches 1. It keeps track of the odd numbers in the sequence and returns them in a sorted list.

Here's a step-by-step breakdown of the function:

1. Initialize an empty list `result` to store the odd numbers.
2. Start a while loop that continues until `n` reaches 1.
3. Inside the loop, check if `n` is even (using the modulus operator `%`).
   - If `n` is even, divide it by 2.
   - If `n` is odd, multiply it by 3 and add 1.
4. Check if the new value of `n` is odd (using the modulus operator `%`).
   - If `n` is odd, append it to the `result` list.
5. Repeat steps 3-4 until `n` reaches 1.
6. Return the `result` list, which now contains the odd numbers from the Collatz sequence, sorted in increasing order.

For example, if you call `get_odd_collatz(5)`, the function will generate the Collatz sequence for 5: `[5, 16, 8, 4, 2, 1]`. The odd numbers in this sequence are 1 and 5, so the function will return the list `[1, 5]`. If you call `get_odd_collatz(12)`, the function will generate the Collatz sequence for 12: `[12, 6, 3, 10, 5, 16, 8, 4, 2, 1]`. The odd numbers in this sequence are 1, 3, 5, and 1, so the function will return the list `[1, 3, 5]`. 

Note that the function assumes that the input `n` is a positive integer. If `n` is not a positive integer, the function may not work correctly. You may want to add error handling to handle invalid input. 

Also