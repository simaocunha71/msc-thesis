import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if (lst == null || lst.isEmpty() || lst.size() < 2) {
            return Optional.empty();
        }
        Set<Integer> set = new HashSet<>(lst);
        if (set.size() < 2) {
            return Optional.empty();
        }
        List<Integer> sortedList = new ArrayList<>(set);
        sortedList.sort(Comparator.naturalOrder());
        return Optional.of(sortedList.get(1));
    }
}