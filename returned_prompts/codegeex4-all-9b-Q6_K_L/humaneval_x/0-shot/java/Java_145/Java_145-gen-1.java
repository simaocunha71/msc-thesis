Here is the solution:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        // create a map to store the sum of digits and index of each number
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.size(); i++) {
            int sum = 0;
            int n = Math.abs(nums.get(i));
            while (n > 0) {
                sum += n % 10;
                n /= 10;
            }
            map.put(nums.get(i), sum);
        }

        // sort the list based on the sum of digits
        Collections.sort(nums, (a, b) -> {
            int sumA = map.get(a);
            int sumB = map.get(b);
            if (sumA != sumB) {
                return sumA - sumB;
            } else {
                return nums.indexOf(a) - nums.indexOf(b);
            }
        });

        return nums;
    }
}
```

This solution first calculates the sum of digits for each number and stores them in a map. Then, it sorts the list based on the sum of digits. If there are several numbers with the same sum of digits, it sorts them based on their index in the original list.