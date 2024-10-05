import java.util.*;

class Solution {
    public List<Integer> rollingMax(List<Integer> numbers) {
        List<Integer> res = new ArrayList<>();
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < numbers.size(); i++) {
            max = Math.max(max, numbers.get(i));
            res.add(max);
        }
        return res;
    }
}
