Here is the solution for the problem:

```java
import java.util.*;

class Solution {
    public int countNums(List<Integer> arr) {
        int count = 0;
        for (int num : arr) {
            int sumOfDigits = getSumOfDigits(num);
            if (sumOfDigits > 0) {
                count++;
            }
        }
        return count;
    }

    private int getSumOfDigits(int num) {
        int sum = 0;
        if (num < 0) {
            num = -num;
        }
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}
```

This solution defines a function `countNums` that takes a list of integers as input and returns the count of numbers in the list whose sum of digits is greater than 0.

The function `getSumOfDigits` is a helper function that calculates the sum of digits of a given integer. If the integer is negative, it first converts it to positive by multiplying it with -1. Then it uses a while loop to extract each digit of the number (by taking the remainder of the number when divided by 10), add it to the sum, and then divide the number by 10 (integer division). The process is repeated until the number becomes 0.

The main function `countNums` iterates over each number in the input list, calculates the sum of its digits using the `getSumOfDigits` function, and increments the count if the sum is greater than 0. Finally, it returns the count.

The unit tests provided in the problem description are used to test the correctness of the solution. The expected output for each test case is provided, and the solution is verified by comparing its output with the expected output. If the output matches the expected output, the test passes; otherwise, it fails. The solution is correct if all the unit tests pass.