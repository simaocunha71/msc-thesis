    The problem is to find the minimum number of elements that need to be changed to make the array palindromic. A palindromic array is an array that is read the same backwards and forwards. In one change, you can change one element to any other element.

    Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public int smallestChange(List<Integer> arr) {
        int n = arr.size();
        int changes = 0;

        // Create a map to store the frequency of each element
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : arr) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // Calculate the frequency of the middle element
        int mid = n / 2;
        int midFreq = 0;
        for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
            if (midFreq < entry.getValue()) {
                midFreq = entry.getValue();
            }
        }

        // Calculate the number of changes needed
        changes = n / 2 - midFreq;
        return changes;
    }
}
```

This solution works by first creating a map to store the frequency of each element in the array. Then, it calculates the frequency of the middle element. The number of changes needed is the difference between the number of elements in the array and the frequency of the middle element.

For example, given the array [1,2,3,5,4,7,9,6], the solution would work as follows:

1. Create a map to store the frequency of each element: {1: 1, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1}
2. Calculate the frequency of the middle element: 1 (since 1 is the most frequent element)
3. Calculate the number of changes needed: 4 (since 4 elements need to be changed to make the array palindromic)

Therefore, the solution returns 4.