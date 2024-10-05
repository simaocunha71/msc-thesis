        int max = -1;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < lst.size(); i++) {
            map.put(lst.get(i), map.getOrDefault(lst.get(i), 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getKey() <= entry.getValue() && entry.getKey() > max) {
                max = entry.getKey();
            }
        }
        return max;
    }
}

In this code, we first create a HashMap to store the frequency of each number in the list. 
Then we iterate over the map entries. For each entry, we check if the key (number) is less than or equal to its value (frequency). 
If so, we compare it with the current maximum (which is initially set to -1), and if it is greater, we update the maximum. 
In the end, we return the maximum. If no number satisfies the condition, the maximum remains -1 and is returned.

The time complexity of this solution is O(n), as we traverse the list twice: once to fill the map, and once to find the maximum. The space complexity is also O(n), as in the worst case we might need to store all n elements in the map.

If we only iterate the list once, we can improve the space complexity to O(1) because we only need to keep track of the current number and its frequency. But it would increase the complexity of the code.

The code works as expected in the examples provided.
*/

//P:
//import java.util.*;
//import java.lang.*;

//class Solution {
//    public int search(List<Integer> lst) {
//        int max = -1;
//        Map<Integer, Integer> map = new HashMap<>();
//        for (int i = 0; i < lst.size(); i++) {
//            map.put(lst.get(i), map.getOrDefault(lst.get(i), 0) + 1);
//        }
//        for (