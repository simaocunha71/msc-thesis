Here is a simple solution in Java that uses a HashSet to store the elements in the array. It then iterates over the array and checks if the current element is not greater than or equal to the element immediately preceding it. If it is, it returns the index of that element. If it doesn't find any such element, it returns -1.

```java
import java.util.*;

class Solution {
    public int canArrange(List<Integer> arr) {
        Set<Integer> set = new HashSet<>();
        for (int num : arr) {
            set.add(num);
        }
        for (int i = 0; i < arr.size(); i++) {
            if (set.contains(arr.get(i-1) + 1)) {
                return i - 1;
            }
        }
        return -1;
    }
}
```

The time complexity of this solution is O(n), where n is the size of the array, because we are iterating over the array twice. The space complexity is also O(n), because we are storing all the elements in the HashSet.