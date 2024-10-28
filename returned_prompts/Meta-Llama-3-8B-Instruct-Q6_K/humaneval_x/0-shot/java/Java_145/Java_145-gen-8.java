Here is the Java solution for the problem. The idea is to first calculate the sum of digits for each number, then sort the list based on these sums and the original index.

```java
import java.util.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        if (nums == null || nums.isEmpty()) {
            return new ArrayList<>();
        }

        List<int[]> list = new ArrayList<>();
        for (int i = 0; i < nums.size(); i++) {
            int num = nums.get(i);
            list.add(new int[]{getSumOfDigits(num), i});
        }

        Collections.sort(list, (a, b) -> {
            if (a[0] != b[0]) {
                return a[0] - b[0];
            } else {
                return a[1] - b[1];
            }
        });

        List<Integer> result = new ArrayList<>();
        for (int[] pair : list) {
            result.add(nums.get(pair[1]));
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

In this solution, we first calculate the sum of digits for each number and store it in a list along with the original index. Then we sort this list based on the sum of digits and the index. Finally, we construct the result list by using the sorted list of indices. The `getSumOfDigits` function is used to calculate the sum of digits for a given number. The time complexity of this solution is O(n log n) due to the sorting operation, where n is the size of the input list. The space complexity is O(n) for storing the list of indices and sums.