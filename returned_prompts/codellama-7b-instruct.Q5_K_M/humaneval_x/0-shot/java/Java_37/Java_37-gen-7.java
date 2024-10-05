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
        List<Integer> ret = new ArrayList<Integer>();
        for(int i=0;i<l.size();i++) {
            if(i%2==0) {
                Collections.sort(ret);
                ret.add(l.get(i));
            } else {
                ret.add(l.get(i));
            }
        }
        return ret;
    }
}
