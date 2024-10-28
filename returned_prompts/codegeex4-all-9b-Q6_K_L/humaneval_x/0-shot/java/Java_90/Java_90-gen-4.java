import java.util.*;
import java.lang.*;

class Solution {
    /**
    You are given a list of integers.
    Write a function nextSmallest() that returns the 2nd smallest element of the list.
    Return null if there is no such element.
    <p>
    nextSmallest(Arrays.asList(1, 2, 3, 4, 5)) == Optional[2]
    nextSmallest(Arrays.asList(5, 1, 4, 3, 2)) == Optional[2]
    nextSmallest(Arrays.asList()) == Optional.empty
    nextSmallest(Arrays.asList(1, 1)) == Optional.empty
     */
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if (lst == null || lst.size() < 2) {
            return Optional.empty();
        }

        Set<Integer> set = new HashSet<>(lst);
        if (set.size() < 2) {
            return Optional.empty();
        }

        List<Integer> sortedList = new ArrayList<>(set);
        Collections.sort(sortedList);

        return Optional.of(sortedList.get(1));
    }
}