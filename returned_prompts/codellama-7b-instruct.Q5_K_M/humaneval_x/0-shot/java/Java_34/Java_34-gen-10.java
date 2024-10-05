import java.util.*;

class Solution {
    public List<Integer> unique(List<Integer> l) {
        Set<Integer> s = new HashSet<Integer>();
        for (int i : l) s.add(i);
        List<Integer> r = new ArrayList<Integer>(s);
        Collections.sort(r);
        return r;
    }
}
