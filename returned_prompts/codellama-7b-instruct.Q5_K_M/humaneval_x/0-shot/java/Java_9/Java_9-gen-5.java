import java.util.*;

class Solution {
    public List<Integer> rollingMax(List<Integer> numbers) {
        List<Integer> result = new ArrayList<Integer>();
        result.add(numbers.get(0));
        for (int i = 1; i < numbers.size(); i++) {
            result.add(Math.max(result.get(i - 1), numbers.get(i)));
        }
        return result;
    }
}
