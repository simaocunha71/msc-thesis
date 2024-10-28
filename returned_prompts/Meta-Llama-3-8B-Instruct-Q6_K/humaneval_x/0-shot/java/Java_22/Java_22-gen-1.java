import java.util.*;

class Solution {
    public List<Integer> filterIntergers(List<Object> values) {
        List<Integer> result = new ArrayList<>();
        for (Object value : values) {
            if (value instanceof Integer) {
                result.add((Integer) value);
            }
        }
        return result;
    }
}