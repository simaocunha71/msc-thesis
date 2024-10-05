import java.util.*;
import java.lang.*;

class Solution {
    public List<String> wordStrings(String s) {
        List<String> words = new ArrayList<>();
        String[] split = s.split("[ ,]+");
        for (String word : split) {
            words.add(word);
        }
        return words;
    }
}