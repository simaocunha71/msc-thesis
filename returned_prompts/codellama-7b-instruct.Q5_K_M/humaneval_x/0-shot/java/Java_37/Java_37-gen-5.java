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

        if (l.size() == 0) return l;
        if (l.size() == 1) return l;
        if (l.size() == 2) {
            if (l.get(0) > l.get(1)) {
                List<Integer> r = new ArrayList<>();
                r.add(l.get(1));
                r.add(l.get(0));
                return r;
            }
            return l;
        }
        if (l.size() == 3) {
            if (l.get(0) > l.get(1)) {
                List<Integer> r = new ArrayList<>();
                r.add(l.get(1));
                r.add(l.get(0));
                r.add(l.get(2));
                return r;
            }
            if (l.get(1) > l.get(2)) {
                List<Integer> r = new ArrayList<>();
                r.add(l.get(0));
                r.add(l.get(2));
                r.add(l.get(1));
                return r;
            }
            return l;
        }
        if (l.size() == 4) {
            if (l.get(0) > l.get(1)) {
                List<Integer> r = new ArrayList<>();
                r.add(l.get(1));
                r.add(l.get(0));