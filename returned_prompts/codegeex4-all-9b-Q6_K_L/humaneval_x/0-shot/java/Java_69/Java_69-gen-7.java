```java
import java.util.*;
import java.lang.*;

class Solution {
    public int search(List<Integer> lst) {
        // Create a map to store the frequency of each number
        Map<Integer, Integer> frequencyMap = new HashMap<>();

        // Populate the map with the frequency of each number
        for (int num : lst) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        // Initialize the greatest integer to -1
        int greatestInteger = -1;

        // Iterate through the map and find the greatest integer with frequency greater than or equal to the value
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            int num = entry.getKey();
            int frequency = entry.getValue();

            if (frequency >= num && num > greatestInteger) {
                greatestInteger = num;
            }
        }

        return greatestInteger;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test cases
        System.out.println(solution.search(Arrays.asList(4, 1, 2, 2, 3, 1))); // Output: 2
        System.out.println(solution.search(Arrays.asList(1, 2, 2, 3, 3, 3, 4, 4, 4))); // Output: 3
        System.out.println(solution.search(Arrays.asList(5, 5, 4, 4, 4))); // Output: -1
    }
}
```