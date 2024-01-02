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
        if (word.length() == 0 || word.charAt(0) != Character.toLowerCase(word.charAt(0)) || word.contains("a")) {return "";}
        char[] alp = word.toCharArray();
        Collections.sort(alp);
        
        for (int i=1;i<word.length()-1;++i){
            if (!word.substring(0,i).contains("a") && !word.substring(i,word.length()).contains("e")){
                return Character.toString((char)alp[i]);
            }
        }
        
        return "";
    }
}