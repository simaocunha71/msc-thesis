import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.

    doubleTheDifference(Arrays.asList(1, 3, 2, 0)) == 1 + 9 + 0 + 0 = 10
    doubleTheDifference(Arrays.asList(-1, -2, 0)) == 0
    doubleTheDifference(Arrays.asList(9, -2)) == 81
    doubleTheDifference(Arrays.asList(0)) == 0

    If the input list is empty, return 0.
     */
    public int doubleTheDifference(List<Object> lst) {
        if (lst == null || lst.isEmpty()) {
            return 0;
        }
        
        Collections.sort(lst);
            
        Map<Integer, Integer> map = new HashMap<>(); // key: index, value : sum
        for (Object obj : lst) {
            if (!map.containsKey((int)obj)) {
                map.put((int)obj, 1);
            } else {
                map.get(obj).add(obj);
            }
        }
        
        int sum = 0;
        for (Object obj : lst) {
            if (map.containsKey((int)obj)) {
                double oddNum = ((Double)map.get((int)obj)).doubleValue();
                sum += Math.pow(oddNum, 2);
            }
        }
        
        return sum;
    }
}