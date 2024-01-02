import java.util.*;
import java.lang.*;

class Solution {
    /**
    Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    canArrange(Arrays.asList(1,2,4,3,5)) = 3
    canArrange(Arrays.asList(1,2,3)) = -1
     */
    public int canArrange(List<Integer> arr) {
        if (arr == null || arr.size() < 2) return -1;
        Map map = new HashMap();
        for (int i=0 ; i<arr.size() ; i++){
            Integer curr = arr.get(i);
            if (!map.containsKey(curr)) {
                map.put(curr, i);
            } else {
                int j = (Integer)map.get(curr);
                while (j <= i){
                    if (arr.get(j).compareTo(curr) == 1){
                        return -1;
                    }
                    j++;
                }
            }
        }
        return (int)(map.size()-1);
    }
}