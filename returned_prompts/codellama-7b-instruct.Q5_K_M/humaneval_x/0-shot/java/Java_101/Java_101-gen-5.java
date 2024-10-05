import java.util.*;

class Solution {
    public List<String> wordStrings(String s) {
        return Arrays.asList(s.split("\\W+"));
    }
}
