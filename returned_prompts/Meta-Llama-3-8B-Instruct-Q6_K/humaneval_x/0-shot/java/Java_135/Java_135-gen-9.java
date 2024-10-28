Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public int canArrange(List<Integer> arr) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i : arr) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }
        int res = -1;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getKey() % 2 == 0) {
                if (map.containsKey(entry.getKey() / 2) && map.get(entry.getKey() / 2) > 0) {
                    res = Math.max(res, entry.getKey() / 2);
                }
            } else {
                if (map.containsKey(entry.getKey() + 1) && map.get(entry.getKey() + 1) > 0) {
                    res = Math.max(res, entry.getKey());
                }
            }
        }
        return res;
    }
}
```
Here, we use a HashMap to store the frequency of each element in the array. Then, we iterate over the map and check if an element is divisible by 2. If it is, we check if there is an element in the map that is half of the current element. If there is, we update the result with the maximum of the current result and the index of the half element. If the element is not divisible by 2, we check if there is an element in the map that is one more than the current element. If there is, we update the result with the maximum of the current result and the index of the current element.

For example, for the input `[1, 2, 4, 3, 5]`, the function returns `3` because the element `4` is not greater than or equal to the element `3` which is immediately preceding it. For the input `[1, 2, 3]`, the function returns `-1` because no such element exists.