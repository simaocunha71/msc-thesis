import java.util.*;
import java.lang.*;

class Solution {
    /**
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than
    zero, and has a frequency greater than or equal to the value of the integer itself.
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search(Arrays.asList(4, 1, 2, 2, 3, 1)) == 2
        search(Arrays.asList(1, 2, 2, 3, 3, 3, 4, 4, 4)) == 3
        search(Arrays.asList(5, 5, 4, 4, 4)) == -1
     */
    public int search(List<Integer> lst) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (Integer num : lst) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }
        int maxNum = -1;
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            if (entry.getKey() > maxNum && entry.getValue() >= entry.getKey()) {
                maxNum = entry.getKey();
            }
        }
        return maxNum;
    }
}