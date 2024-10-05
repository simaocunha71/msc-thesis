import java.util.*;

class Solution {
    public List<String> wordStrings(String s) {
        String[] words = s.split("\\s*,\\s*");
        return Arrays.asList(words);
    }
}
