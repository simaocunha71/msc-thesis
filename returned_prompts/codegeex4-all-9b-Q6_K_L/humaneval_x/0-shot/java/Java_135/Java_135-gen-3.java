Here is a Java solution using a HashMap to track the frequency of each element in the array. We then iterate through the array and check if the current element has a preceding element. If it does, we decrement the frequency of the preceding element in the HashMap. If the frequency of the preceding element becomes negative, we return the current index. If we reach the end of the array without returning, we return -1.

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int canArrange(List<Integer> arr) {
        HashMap<Integer, Integer> frequencyMap = new HashMap<>();
        for (Integer num : arr) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }
        for (int i = 0; i < arr.size(); i++) {
            Integer num = arr.get(i);
            if (frequencyMap.containsKey(num - 1)) {
                frequencyMap.put(num - 1, frequencyMap.get(num - 1) - 1);
                if (frequencyMap.get(num - 1) < 0) {
                    return i;
                }
            }
        }
        return -1;
    }
}
```

This solution has a time complexity of O(n) and a space complexity of O(n), where n is the length of the array.