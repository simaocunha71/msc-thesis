import java.util.*;
import java.lang.*;

class Solution {
    public String findMax(List<String> words) {
        if (words == null || words.isEmpty()) return "";
        String maxWord = words.get(0);
        int maxUniqueChars = countUniqueChars(maxWord);
        for (String word : words) {
            int uniqueChars = countUniqueChars(word);
            if (uniqueChars > maxUniqueChars) {
                maxUniqueChars = uniqueChars;
                maxWord = word;
            } else if (uniqueChars == maxUniqueChars) {
                if (word.compareTo(maxWord) < 0) {
                    maxWord = word;
                }
            }
        }
        return maxWord;
    }

    private int countUniqueChars(String word) {
        Set<Character> uniqueChars = new HashSet<>();
        for (char c : word.toCharArray()) {
            uniqueChars.add(c);
        }
        return uniqueChars.size();
    }
}