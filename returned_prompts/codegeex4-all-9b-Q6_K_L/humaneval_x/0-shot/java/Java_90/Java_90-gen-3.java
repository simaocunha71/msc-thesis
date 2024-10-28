import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if (lst == null || lst.size() < 2) {
            return Optional.empty();
        }
        Set<Integer> set = new HashSet<>(lst);
        List<Integer> sortedList = new ArrayList<>(set);
        Collections.sort(sortedList);
        if (sortedList.size() < 2) {
            return Optional.empty();
        }
        return Optional.of(sortedList.get(1));
    }
}