import java.util.*;
import java.lang.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        if (s == null || s.isEmpty()) {
            return Collections.emptyList();
        }
        String[] words = s.split(" ");
        List<String> result = new ArrayList<>();
        for (String word : words) {
            int consonantCount = 0;
            for (char c : word.toCharArray()) {
                if (isConsonant(c)) {
                    consonantCount++;
                }
            }
            if (consonantCount == n) {
                result.add(word);
            }
        }
        return result;
    }

    private boolean isConsonant(char c) {
        c = Character.toLowerCase(c);
        return c >= 'b' && c <= 'z' && c != 'e' && c != 'i' && c != 'o' && c != 'u';
    }
}