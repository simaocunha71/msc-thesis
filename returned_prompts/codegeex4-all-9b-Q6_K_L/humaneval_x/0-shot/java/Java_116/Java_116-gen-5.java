import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortArray(List<Integer> arr) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < arr.size(); i++) {
            map.put(arr.get(i), Integer.bitCount(arr.get(i)));
        }
        Collections.sort(arr, (a, b) -> {
            if (map.get(a).equals(map.get(b))) {
                return a - b;
            } else {
                return map.get(a) - map.get(b);
            }
        });
        return arr;
    }
}