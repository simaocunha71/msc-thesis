    import java.util.*;

public class Solution {
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if (lst.isEmpty()) {
            return Optional.empty();
        }
        Integer min = lst.get(0);
        Integer secondMin = null;
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < min) {
                secondMin = min;
                min = lst.get(i);
            } else if (lst.get(i) < secondMin) {
                secondMin = lst.get(i);
            }
        }
        if (secondMin == null) {
            return Optional.empty();
        }
        return Optional.of(secondMin);
    }
}
