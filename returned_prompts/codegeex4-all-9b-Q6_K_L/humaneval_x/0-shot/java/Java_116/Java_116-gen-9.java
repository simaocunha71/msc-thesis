import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortArray(List<Integer> arr) {
        Comparator<Integer> comparator = new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                int count1 = Integer.bitCount(o1);
                int count2 = Integer.bitCount(o2);
                if (count1 != count2) {
                    return Integer.compare(count1, count2);
                } else {
                    return Integer.compare(o1, o2);
                }
            }
        };
        Collections.sort(arr, comparator);
        return arr;
    }
}