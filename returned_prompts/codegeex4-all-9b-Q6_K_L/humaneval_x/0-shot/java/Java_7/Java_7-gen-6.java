import java.util.*;
import java.lang.*;

class Solution {
    public List<String> filterBySubstring(List<String> strings, String substring) {
        List<String> res = new ArrayList<>();
        for (String s : strings) {
            if (s.contains(substring)) {
                res.add(s);
            }
        }
        return res;
    }
}