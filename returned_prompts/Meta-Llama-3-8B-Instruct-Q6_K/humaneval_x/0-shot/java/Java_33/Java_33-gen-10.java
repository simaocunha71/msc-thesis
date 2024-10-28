    import java.util.*;
    import java.lang.*;

class Solution {
    public List<Integer> sortThird(List<Integer> l) {
        List<Integer> l1 = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                l1.add(l.get(i));
            } else {
                l1.add(i % 3 == 0 ? Collections.min(l) : l.get(i));
            }
        }
        return l1;
    }
}
