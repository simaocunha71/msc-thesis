Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public int countNums(List<Integer> arr) {
        int count = 0;
        for (int num : arr) {
            int sumDigits = getSumOfDigits(num);
            if (sumDigits > 0) {
                count++;
            }
        }
        return count;
    }

    private int getSumOfDigits(int num) {
        int sum = 0;
        boolean isNegative = false;
        if (num < 0) {
            isNegative = true;
            num = -num;
        }
        while (num > 0) {
            int digit = num % 10;
            sum += digit;
            num /= 10;
        }
        return isNegative ? -sum : sum;
    }
}
```
The function `countNums` iterates over the input array and for each number, it calculates the sum of its digits using the helper function `getSumOfDigits`. If the sum is positive, it increments the count. Finally, it returns the count.

The function `getSumOfDigits` calculates the sum of digits of a number. If the number is negative, it sets a flag `isNegative` and converts the number to its absolute value. Then, it iterates over the digits of the number (from right to left) and adds each digit to the sum. If the original number was negative, it negates the sum. The function returns the sum.

The unit tests provided in the problem statement are used to verify the correctness of the solution. For example, the test `>>> countNums(Arrays.asList()) == 0` checks that the function returns 0 when the input array is empty. Similarly, the tests `>>> countNums(Arrays.asList(-1, 11, -11)) == 1` and `>>> countNums(Arrays.asList(1, 1, 2)) == 3` check that the function correctly counts the numbers with sum of digits greater than 0 in the input arrays.