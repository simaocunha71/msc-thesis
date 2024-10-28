        int max = -1;
        Map<Integer, Integer> map = new HashMap<>();
        for (int n : lst) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getKey() <= entry.getValue()) {
                max = Math.max(max, entry.getKey());
            }
        }
        return max;
    }
}

The solution works by first creating a map where the keys are the unique numbers in the list and the values are their respective frequencies. It then iterates through each entry in the map. If the key (the number) is less than or equal to the value (its frequency), it means this number occurs at least as often as its value, so it's a potential candidate for the result. It updates the result with the maximum of the current result and the key. If no potential candidate is found after checking all entries, it returns -1.

*/

//Java solution

import java.util.*;
import java.lang.*;

class Solution {
    public int search(List<Integer> lst) {
        int max = -1;
        Map<Integer, Integer> map = new HashMap<>();
        for (int n : lst) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getKey() <= entry.getValue()) {
                max = Math.max(max, entry.getKey());
            }
        }
        return max;
    }
}

//Test cases

import java.util.*;
import java.lang.*;

public class Test {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.search(Arrays.asList(4, 1, 2, 2, 3, 1))); // Output: 2
        System.out.println(s.search(Arrays.asList(1, 2,