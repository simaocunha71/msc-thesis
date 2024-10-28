import java.util.*;

class Solution {
    public List<Integer> unique(List<Integer> l) {
        List<Integer> result = new ArrayList<Integer>();
        Set<Integer> seen = new HashSet<Integer>();
        for (int i : l) {
            if (!seen.contains(i)) {
                result.add(i);
                seen.add(i);
            }
        }
        return result;
    }
}
