import java.util.*;
import java.lang.*;

class Solution {
    /**
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sortEven(Arrays.asList(1, 2, 3))
    [1, 2, 3]
    >>> sortEven(Arrays.asList(5, 6, 3, 4))
    [3, 6, 5, 4]
     */
    public List<Integer> sortEven(List<Integer> l) {
        // Complete this function
        List<Integer> l1 = new ArrayList<Integer>();
        List<Integer> l2 = new ArrayList<Integer>();
        List<Integer> l3 = new ArrayList<Integer>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                l1.add(l.get(i));
            } else {
                l2.add(l.get(i));
            }
        }
        l3.addAll(l1);
        Collections.sort(l2);
        l3.addAll(l2);
        return l3;
    }
}
