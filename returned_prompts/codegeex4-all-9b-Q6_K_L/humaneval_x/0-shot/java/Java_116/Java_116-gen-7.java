import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortArray(List<Integer> arr) {
        return arr.stream()
                .sorted((o1, o2) -> {
                    int count1 = Integer.bitCount(o1);
                    int count2 = Integer.bitCount(o2);
                    return count1 == count2 ? o1 - o2 : count1 - count2;
                })
                .collect(Collectors.toList());
    }
}