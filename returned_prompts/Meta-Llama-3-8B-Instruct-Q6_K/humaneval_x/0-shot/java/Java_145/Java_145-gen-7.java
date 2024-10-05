```java
import java.util.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        nums.sort((a, b) -> {
            int sumA = getDigitSum(a);
            int sumB = getDigitSum(b);
            if (sumA != sumB) {
                return Integer.compare(sumA, sumB);
            } else {
                return Integer.compare(nums.indexOf(a), nums.indexOf(b));
            }
        });
        return nums;
    }

    private int getDigitSum(int n) {
        int sum = 0;
        while (n != 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}
```


Explanation:
This solution uses Java's built-in `sort` method for lists, which sorts the list in-place. It uses a custom comparator to sort the list. The comparator takes two integers `a` and `b` as input, calculates the sum of their digits using the `getDigitSum` method, and compares these sums. If the sums are different, it compares them and returns the result. If the sums are the same, it compares the indices of `a` and `b` in the original list using `nums.indexOf(a)` and `nums.indexOf(b)`, and returns the result.

The `getDigitSum` method calculates the sum of the digits of a given integer `n` by repeatedly taking the remainder of `n` divided by 10 (which gives the last digit of `n`), adding this digit to a running sum, and then dividing `n` by 10 to remove the last digit. This process is repeated until `n` becomes 0.

The `orderByPoints` method sorts the input list `nums` using this custom comparator, and returns the sorted list. If the input list is empty, it returns an empty list. If all elements in the input list have the same sum of digits, the list is sorted based on the original order of the elements. Otherwise, the list is sorted based on the sum of digits.