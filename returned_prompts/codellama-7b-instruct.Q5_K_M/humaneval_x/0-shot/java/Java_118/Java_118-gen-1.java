import java.util.*;
import java.lang.*;

class Solution {
    /**
    You are given a word. Your task is to find the closest vowel that stands between
    two consonants from the right side of the word (case sensitive).

    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition.

    You may assume that the given string contains English letter only.

    Example:
    getClosestVowel("yogurt") ==> "u"
    getClosestVowel("FULL") ==> "U"
    getClosestVowel("quick") ==> ""
    getClosestVowel("ab") ==> ""
     */
    public String getClosestVowel(String word) {
        int len = word.length();
        for (int i = len-1; i >= 0; i--) {
            if (isConsonant(word.charAt(i))) {
                for (int j = i - 1; j >= 0; j--) {
                    if (isVowel(word.charAt(j))) {
                        return String.valueOf(word.charAt(j));
                    }
                }
            }
        }
        return "";
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    private boolean isConsonant(char c) {
        return !isVowel(c);
    }
}
