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
        Map<Character, Character> vowels = new HashMap<>();
        for (int i = 0; i < word.length(); i++) { // add vowels to the map
            Character c = word.charAt(i); // get the current character
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                vowels.put(c, c);
            }
        }
        
        int first_consonant = Integer.MIN_VALUE; // set the first consonant to be the end of string in word list (empty string)
        for (int i = 0; i < word.length(); i++) { // search for vowels in between two consecutive characters from right side and update them as well
            Character c = word.charAt(i); // get the current character
            if (!vowels.containsKey(c)) continue; // don't update empty string
            
            int first_consonant_current = Integer.compareUnsigned(Integer.MIN_VALUE, i); // compare with previous value and set it to be lower than previous value
            Character current = word.charAt(i); // get the current character
            
            if (first_consonant < 0) { first_consonant = Integer.minValue(); } // reset first consonant to beginning of word
           