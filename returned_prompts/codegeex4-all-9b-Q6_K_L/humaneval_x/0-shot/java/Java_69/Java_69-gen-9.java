import java.util.*;
import java.lang.*;

class Solution {
    public int search(List<Integer> lst) {
        // TODO: write your code here
        Map<Integer, Integer> map = new HashMap<>();
        for (Integer num : lst) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        int max = -1;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getValue() >= entry.getKey() && entry.getKey() > max) {
                max = entry.getKey();
            }
        }
        return max;
    }
}