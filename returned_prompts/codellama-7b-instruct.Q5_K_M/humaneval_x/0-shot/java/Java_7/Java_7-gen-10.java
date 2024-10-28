import java.util.*;

class Solution {
    public List<String> filterBySubstring(List<String> strings, String substring) {
        List<String> filtered = new ArrayList<>();
        for (String s : strings) {
            if (s.contains(substring)) {
                filtered.add(s);
            }
        }
        return filtered;
    }
}
