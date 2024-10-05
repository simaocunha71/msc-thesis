import java.util.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        List<String> result = new ArrayList<>();
        if (s == null || s.length() == 0) {
            return result;
        }
        String[] words = s.split("\\s+");
        for (String word : words) {
            if (word.length() == n) {
                result.add(word);
            }
        }
        return result;
    }
}
