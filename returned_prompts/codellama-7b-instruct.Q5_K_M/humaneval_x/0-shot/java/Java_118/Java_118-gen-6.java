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
        if (len == 0) {
            return "";
        }
        int start = 0;
        while (start < len && !isConsonant(word.charAt(start))) {
            start++;
        }
        if (start == len) {
            return "";
        }
        int end = len - 1;
        while (end >= start && !isConsonant(word.charAt(end))) {
            end--;
        }
        if (end < start) {
            return "";
        }
        int min = Integer.MAX_VALUE;
        char closest = ' ';
        for (int i = end + 1; i < len; i++) {
            char c = word.charAt(i);
            if (isVowel(c)) {
                int dis = i - end;
                if (dis < min) {
                    min = dis;
                    closest = c;
                }
            }
        }
        if (min == Integer.MAX_VALUE) {
            return "";
        }
        return "" + closest;
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' ||