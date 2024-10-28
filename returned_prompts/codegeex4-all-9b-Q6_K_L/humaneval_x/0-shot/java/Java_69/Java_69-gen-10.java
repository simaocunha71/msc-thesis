```java
import java.util.*;
import java.lang.*;

class Solution {
    public int search(List<Integer> lst) {
        // Create a HashMap to store the frequency of each integer
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : lst) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        // Initialize the greatest integer to -1
        int greatestInteger = -1;

        // Iterate through the frequency map
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            int num = entry.getKey();
            int freq = entry.getValue();

            // If the frequency of the current integer is greater than or equal to the integer itself,
            // and it is greater than the current greatest integer, update the greatest integer
            if (freq >= num && num > greatestInteger) {
                greatestInteger = num;
            }
        }

        // Return the greatest integer
        return greatestInteger;
    }
}
```