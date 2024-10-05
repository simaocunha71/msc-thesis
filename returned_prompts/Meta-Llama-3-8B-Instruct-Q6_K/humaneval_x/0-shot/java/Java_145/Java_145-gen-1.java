Here is a solution in Java:

```java
import java.util.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        if (nums == null || nums.isEmpty()) {
            return new ArrayList<>();
        }

        Comparator<Integer> comparator = new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                int sumA = getSumOfDigits(a);
                int sumB = getSumOfDigits(b);
                if (sumA == sumB) {
                    return Integer.compare(nums.indexOf(a), nums.indexOf(b));
                } else {
                    return Integer.compare(sumA, sumB);
                }
            }

            private int getSumOfDigits(int n) {
                int sum = 0;
                while (n != 0) {
                    sum += n % 10;
                    n /= 10;
                }
                return sum;
            }
        };

        Collections.sort(nums, comparator);
        return nums;
    }
}
```

Explanation:
The solution uses a custom comparator to sort the list of integers. The comparator compares two integers based on the sum of their digits. If the sum of the digits is the same, it compares the integers based on their original index in the list.

The `getSumOfDigits` method is used to calculate the sum of the digits of a given integer. It uses a while loop to extract the digits of the integer and add them up.

The `orderByPoints` method first checks if the input list is null or empty, and returns an empty list in this case. Then it creates a comparator and uses it to sort the list. Finally, it returns the sorted list.

Note that this solution assumes that the input list contains only integers. If the list can contain other types of objects, additional error checking may be needed.