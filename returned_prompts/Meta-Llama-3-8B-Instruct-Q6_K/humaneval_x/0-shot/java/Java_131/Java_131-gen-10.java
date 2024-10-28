        int res = 1;
        while (n > 0) {
            int digit = n % 10;
            if (digit % 2 != 0) {
                res *= digit;
            }
            n /= 10;
        }
        return res;
    }
}

S:
The problem asks to find the product of all the odd digits in a given integer. If all digits are even, return 0.

The solution is to use a while loop to iterate through the digits of the integer from right to left. For each digit, check if it's odd (i.e., if the remainder of the digit divided by 2 is not 0). If it's odd, multiply the result by the digit. If no odd digits are found, return 0.

Here's the Java code for the solution:

```java
public int digits(int n) {
    int res = 1;
    while (n > 0) {
        int digit = n % 10;
        if (digit % 2 != 0) {
            res *= digit;
        }
        n /= 10;
    }
    return res;
}
```

This code works by using the modulus operator (`%`) to get the remainder of the integer divided by 10, which gives the last digit. It then checks if the digit is odd by using the modulus operator again to see if the remainder of the digit divided by 2 is not 0. If the digit is odd, it multiplies the result by the digit. Finally, it divides the integer by 10 to move to the next digit. The process is repeated until there are no more digits. If no odd digits are found, the result is 0. If odd digits are found, the result is the product of all the odd digits.