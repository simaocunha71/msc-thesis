import java.util.*;

class Solution {
    public List<Integer> uniqueDigits(List<Integer> x) {
        List<Integer> result = new ArrayList<>();
        for (int i : x) {
            if (i % 2 != 0) result.add(i);
        }
        return result;
    }
}
