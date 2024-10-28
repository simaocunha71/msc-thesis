Here is the solution:

```java
import java.util.*;

class Solution {
    public List<Integer> pluck(List<Integer> arr) {
        List<Integer> result = new ArrayList<>();
        if (arr.isEmpty()) {
            return result;
        }
        
        int minEvenValue = Integer.MAX_VALUE;
        int minEvenIndex = -1;
        
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < minEvenValue) {
                minEvenValue = arr.get(i);
                minEvenIndex = i;
            }
        }
        
        if (minEvenIndex != -1) {
            result.add(minEvenValue);
            result.add(minEvenIndex);
        }
        
        return result;
    }
}
```

Explanation:
The solution iterates over the given array and finds the smallest even value. If no even values are found, it returns an empty list. If an even value is found, it also finds the index of that value. The result is a list containing the smallest even value and its index. If the array is empty, it returns an empty list.

Time complexity: O(n), where n is the size of the input array. This is because we iterate over the array once.

Space complexity: O(1), as we are using a constant amount of space to store the result. The size of the input array does not affect the space complexity. 