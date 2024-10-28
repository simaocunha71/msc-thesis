Here is the solution:
```java
import java.util.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        // Create a list of pairs, where each pair contains the number and its sum of digits
        List<int[]> pairs = new ArrayList<>();
        for (int num : nums) {
            int sumOfDigits = getSumOfDigits(num);
            pairs.add(new int[]{sumOfDigits, num});
        }

        // Sort the list of pairs based on the sum of digits and the original index
        pairs.sort(Comparator.comparingInt(a -> a[0]).thenComparingInt(a -> nums.indexOf(a[1])));

        // Create a new list and add the sorted numbers
        List<Integer> result = new ArrayList<>();
        for (int[] pair : pairs) {
            result.add(pair[1]);
        }

        return result;
    }

    private int getSumOfDigits(int num) {
        int sum = 0;
        while (num != 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}
```
The solution works by first creating a list of pairs, where each pair contains the number and its sum of digits. Then, it sorts this list of pairs based on the sum of digits and the original index of the number. Finally, it creates a new list and adds the sorted numbers to it.

The `getSumOfDigits` method calculates the sum of the digits of a given integer. It does this by repeatedly taking the remainder of the number when divided by 10 (which gives the last digit), adding this to the sum, and then dividing the number by 10 to remove the last digit.

The `orderByPoints` method uses the `Comparator` interface to sort the list of pairs. It first sorts the list based on the sum of digits, and then sorts the list based on the original index of the number. This ensures that numbers with the same sum of digits are sorted based on their original index. The `thenComparingInt` method is used to specify the second sorting criterion. In this case, it is the original index of the number. The `Comparator.comparingInt` method is used to specify the first sorting criterion, which is the sum of digits. The `sort` method is used to sort the list of pairs based on the comparator. Finally, the method creates a new list and adds the sorted numbers to it.