```java
import java.util.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        Collections.sort(nums, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                int sumA = sumOfDigits(a);
                int sumB = sumOfDigits(b);
                if (sumA != sumB) {
                    return Integer.compare(sumA, sumB);
                } else {
                    return Integer.compare(nums.indexOf(a), nums.indexOf(b));
                }
            }

            private int sumOfDigits(int n) {
                int sum = 0;
                while (n != 0) {
                    sum += n % 10;
                    n /= 10;
                }
                return sum;
            }
        });
        return nums;
    }
}
```


Explanation:

This solution sorts the list of integers using the `Collections.sort()` method and a custom comparator. The comparator compares two integers based on their sum of digits. If the sum of digits is different, it compares the integers based on their sum of digits. If the sum of digits is the same, it compares the integers based on their original index in the list.

The `sumOfDigits()` method is used to calculate the sum of digits of an integer. It uses a while loop to extract each digit of the integer by taking the remainder of the integer when divided by 10, and then divides the integer by 10 to move to the next digit. The sum of digits is calculated by adding each extracted digit to a running total.

The `orderByPoints()` method sorts the list of integers according to the sum of their digits and returns the sorted list. It uses the custom comparator to sort the list and returns the sorted list. If the list is empty, it returns an empty list.