import java.util.*;
import java.lang.*;

class Solution {
    public int search(List<Integer> lst) {

        // Create a map to store the frequency of each integer
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : lst) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        // Iterate through the map to find the greatest integer with frequency greater than or equal to the integer itself
        int greatestInt = -1;
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            int num = entry.getKey();
            int freq = entry.getValue();
            if (freq >= num && num > greatestInt) {
                greatestInt = num;
            }
        }

        return greatestInt;
    }
}