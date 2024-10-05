import java.util.*;

class Solution {
    public static List<String> selectWords(String s, int n) {
        List<String> words = new ArrayList<>();
        for (String word : s.split(" ")) {
            if (countVowels(word) == n) {
                words.add(word);
            }
        }
        return words;
    }

    private static int countVowels(String word) {
        int count = 0;
        for (char ch : word.toCharArray()) {
            if (isVowel(ch)) {
                count++;
            }
        }
        return count;
    }

    private static boolean isVowel(char ch) {
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
    }
}
