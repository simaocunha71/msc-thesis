import java.util.*;
import java.lang.*;

class Solution {
    public String findMax(List<String> words) {
        String maxWord = "";
        int maxUniqueChars = 0;

        for (String word : words) {
            int uniqueChars = getUniqueCharCount(word);
            if (uniqueChars > maxUniqueChars || (uniqueChars == maxUniqueChars && word.compareTo(maxWord) < 0)) {
                maxUniqueChars = uniqueChars;
                maxWord = word;
            }
        }

        return maxWord;
    }

    private int getUniqueCharCount(String word) {
        Set<Character> uniqueChars = new HashSet<>();
        for (char c : word.toCharArray()) {
            uniqueChars.add(c);
        }
        return uniqueChars.size();
    }
}