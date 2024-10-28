Here is a simple solution using Java:

```java
import java.util.*;

class Solution {
    public List<Integer> maximum(List<Integer> arr, int k) {
        // Sort the list in descending order
        Collections.sort(arr, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                return b.compareTo(a);
            }
        });

        // Return a new list with the first k elements
        return arr.subList(0, k);
    }
}
```
This solution works by first sorting the list in descending order, which means the largest numbers will be at the beginning of the list. Then, it returns a new list that contains the first k elements of the sorted list, which are the k largest numbers. The time complexity of this solution is O(n log n) due to the sorting, where n is the length of the input list. The space complexity is O(1) because it only uses a constant amount of space to store the result.