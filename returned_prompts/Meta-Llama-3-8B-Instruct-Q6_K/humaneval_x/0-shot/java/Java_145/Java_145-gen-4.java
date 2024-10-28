```java
import java.util.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        if (nums == null || nums.isEmpty()) {
            return nums;
        }

        nums.sort((a, b) -> {
            int sumA = sumOfDigits(a);
            int sumB = sumOfDigits(b);

            if (sumA == sumB) {
                return Integer.compare(nums.indexOf(a), nums.indexOf(b));
            } else {
                return Integer.compare(sumA, sumB);
            }
        });

        return nums;
    }

    private int sumOfDigits(int num) {
        int sum = 0;
        while (num != 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}
```
Explanation:
In this solution, we use the sort method of List interface and provide a custom comparator. The comparator compares two numbers based on their sum of digits. If the sum of digits is the same for both numbers, it compares their original indices in the list.

We define a helper method `sumOfDigits` to calculate the sum of digits of a given number.

Finally, we return the sorted list. If the list is empty, we return the original list as it is already sorted.

The time complexity of this solution is O(n log n) due to the sorting operation, where n is the size of the input list. The space complexity is O(1) as we are not using any additional space that scales with the input size. 