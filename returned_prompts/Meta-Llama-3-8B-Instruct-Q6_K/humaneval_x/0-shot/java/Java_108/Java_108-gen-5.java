Here is a Java function that counts the number of elements in the given array that have a sum of digits greater than 0. If a number is negative, it considers the first signed digit as negative.

```java
import java.util.*;

public class Solution {
    public int countNums(List<Integer> arr) {
        int count = 0;
        for (int num : arr) {
            int sum = getSumOfDigits(num);
            if (sum > 0) {
                count++;
            }
        }
        return count;
    }

    private int getSumOfDigits(int num) {
        int sum = 0;
        while (num != 0) {
            int digit = num % 10;
            if (num < 0) {
                digit = -digit;
            }
            sum += digit;
            num /= 10;
        }
        return sum;
    }
}
```

In this solution, we define a helper function `getSumOfDigits` to calculate the sum of digits of a given number. We then iterate through the array, calculate the sum of digits for each number, and increment the count if the sum is greater than 0. Finally, we return the count. The `getSumOfDigits` function uses a while loop to extract each digit from the number, and adds it to the sum. If the number is negative, it negates the first digit. The function returns the sum of digits. The `countNums` function then iterates through the array, calculates the sum of digits for each number, and increments the count if the sum is greater than 0. Finally, it returns the count. 