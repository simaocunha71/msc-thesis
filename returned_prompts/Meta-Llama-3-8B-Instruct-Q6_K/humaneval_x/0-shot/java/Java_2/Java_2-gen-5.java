    return number - Math.floor(number);
    }

Explanation:
The problem is asking to truncate the given floating point number into its integer part and decimal part. The decimal part is the leftover part always smaller than 1.

To solve this problem, we can use the built-in `Math.floor()` function in Java which returns the largest integer less than or equal to the given number. Then, we subtract this integer from the original number to get the decimal part.

For example, if the input is 3.5, `Math.floor(3.5)` returns 3, so `3.5 - 3` is 0.5, which is the decimal part. Similarly, for the input 4.9, `Math.floor(4.9)` returns 4, so `4.9 - 4` is 0.9, which is the decimal part. 

This solution works for all positive floating point numbers. The `Math.floor()` function handles both integer and non-integer parts correctly, and the subtraction operation ensures that the decimal part is returned. 