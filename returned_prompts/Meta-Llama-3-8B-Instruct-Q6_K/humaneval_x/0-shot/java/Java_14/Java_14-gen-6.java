import java.util.*;

public class Solution {

    public List<String> allPrefixes(String s) {
        List<String> result = new ArrayList<>();
        for (int i = 1; i <= s.length(); i++) {
            result.add(s.substring(0, i));
        }
        return result;
    }
}
