```java
import java.util.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        Collections.sort(nums, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                int sumA = sumOfDigits(a);
                int sumB = sumOfDigits(b);

                if (sumA != sumB) {
                    return Integer.compare(sumA, sumB);
                } else {
                    return Integer.compare(nums.indexOf(a), nums.indexOf(b));
                }
            }

            private int sumOfDigits(int num) {
                int sum = 0;
                while (num != 0) {
                    sum += num % 10;
                    num /= 10;
                }
                return sum;
            }
        });
        return nums;
    }
}
```


Explanation:
The task is to sort the list of integers based on the sum of their digits. If there are multiple integers with the same sum of digits, sort them based on their original order.

Here is a Java solution using the `Collections.sort()` method and a custom comparator. The comparator compares two integers based on the sum of their digits. If the sums are equal, it compares the original indices of the integers.

The `sumOfDigits()` method calculates the sum of the digits of an integer by repeatedly taking the remainder of the integer when divided by 10 (to get the last digit) and adding it to the sum, then dividing the integer by 10 to remove the last digit, until the integer becomes 0.

In the `compare()` method, we first calculate the sums of the digits of the two integers. If the sums are not equal, we compare them directly. If the sums are equal, we compare the original indices of the integers. This ensures that integers with the same sum of digits are sorted based on their original order.

Finally, we return the sorted list of integers.