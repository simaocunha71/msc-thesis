Here is the solution to the problem:

```java
import java.util.*;

class Solution {
    public int countNums(List<Integer> arr) {
        int count = 0;
        for (int num : arr) {
            if (num < 0) {
                num = -num; // convert to positive
            }
            int sum = 0;
            while (num > 0) {
                sum += num % 10; // add the last digit to the sum
                num /= 10; // remove the last digit
            }
            if (sum > 0) {
                count++; // increment the count if the sum is positive
            }
        }
        return count;
    }
}
```



Explanation:

*   We iterate over each number in the input array.
*   If the number is negative, we convert it to positive by multiplying it by -1.
*   We calculate the sum of the digits of the number using a while loop.
*   If the sum of the digits is greater than 0, we increment the count.
*   Finally, we return the count of numbers with a sum of digits greater than 0.