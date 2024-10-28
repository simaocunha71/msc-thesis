import java.util.*;

class Solution {
    public List<Integer> filterIntergers(List<Object> values) {
        return values.stream().filter(o -> o instanceof Integer).map(o -> (Integer) o).collect(Collectors.toList());
    }
}
