Here is the Java code for the problem:

```java
import java.util.*;

public class Solution {
    public int countNums(List<Integer> arr) {
        int count = 0;
        for (int num : arr) {
            if (num > 0) {
                int sum = getSumOfDigits(Math.abs(num));
                if (sum > 0) {
                    count++;
                }
            } else if (num < 0) {
                int sum = getSumOfDigits(num);
                if (sum > 0) {
                    count++;
                }
            }
        }
        return count;
    }

    private int getSumOfDigits(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}
```

In this solution, we iterate through each number in the array. If the number is positive, we calculate the sum of its digits using the `getSumOfDigits` method and increment the count if the sum is greater than 0. If the number is negative, we calculate the sum of its digits considering the negative sign as a digit, and increment the count if the sum is greater than 0. Finally, we return the count.

The `getSumOfDigits` method calculates the sum of the digits of a number by repeatedly taking the remainder of the number when divided by 10 (which gives the last digit), adding it to the sum, and then dividing the number by 10 to move to the next digit. This process continues until the number becomes 0. The sum of the digits is then returned.