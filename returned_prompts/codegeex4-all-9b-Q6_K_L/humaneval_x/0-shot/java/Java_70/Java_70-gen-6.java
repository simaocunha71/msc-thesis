import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strangeSortList(Arrays.asList(1, 2, 3, 4)) == Arrays.asList(1, 4, 2, 3)
    strangeSortList(Arrays.asList(5, 5, 5, 5)) == Arrays.asList(5, 5, 5, 5)
    strangeSortList(Arrays.asList()) == Arrays.asList()
     */
    public List<Integer> strangeSortList(List<Integer> lst) {
        Collections.sort(lst);
        List<Integer> result = new ArrayList<>();
        int i = 0;
        while (i < lst.size()) {
            result.add(lst.get(i));
            i += 2;
        }
        i = 1;
        while (i < lst.size()) {
            result.add(lst.get(i));
            i += 2;
        }
        return result;
    }
}