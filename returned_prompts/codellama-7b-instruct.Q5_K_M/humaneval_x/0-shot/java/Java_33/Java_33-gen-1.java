import java.util.*;
import java.lang.*;

class Solution {
    /**
    This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sortThird(Arrays.asList(1, 2, 3))
    [1, 2, 3]
    >>> sortThird(Arrays.asList(5, 6, 3, 4, 8, 9, 2))
    [2, 6, 3, 4, 8, 9, 5]
     */
    public List<Integer> sortThird(List<Integer> l) {
        List<Integer> l1 = new ArrayList<Integer>();
        List<Integer> l2 = new ArrayList<Integer>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0)
                l1.add(l.get(i));
            else
                l2.add(l.get(i));
        }
        l1.sort(null);
        l2.sort(null);
        List<Integer> l3 = new ArrayList<Integer>();
        for (int i = 0; i < l1.size(); i++) {
            l3.add(l1.get(i));
        }
        for (int i = 0; i < l2.size(); i++) {
            l3.add(l2.get(i));
        }
        return l3;
    }
}
