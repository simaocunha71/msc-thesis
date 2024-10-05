        int lastDigitA = Math.abs(a) % 10;
        int lastDigitB = Math.abs(b) % 10;
        return lastDigitA * lastDigitB;
    }
}

Explanation:
The function multiply takes two integers a and b as input. It calculates the last digit of each integer by using the modulo operator with 10 (a % 10 and b % 10). The modulo operator returns the remainder of division of a number by 10. The absolute value of a and b is taken using Math.abs in order to handle negative numbers. Then the function returns the product of the two last digits.

The last digit of a number is always the remainder of the number when divided by 10. This is due to the fact that the remainder of division of a number by 10 gives the last digit of that number.

Note: This solution assumes that the input is always valid. If the input could be invalid (like a negative number), you would need to add error checking to handle that.

This solution has a time complexity of O(1) as it performs a constant number of operations regardless of the size of the input.

This solution has a space complexity of O(1) as it uses a constant amount of space.

This solution is written in Java.
 */

// 2020-04-07 15:55:57

// 2020-04-07 15:55:57

// 2020-04-07 15:55:57

// 2020-04-07 15:55:57

// 2020-04-07 15:55:57

// 2020-04-07 15:55:57

// 2020-04-07 15:55:57

// 2020-04-07 15:55:57

// 2020-04-07 15:55:57
