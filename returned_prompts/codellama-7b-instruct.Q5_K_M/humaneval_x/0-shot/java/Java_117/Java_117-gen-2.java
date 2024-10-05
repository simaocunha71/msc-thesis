import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a string s and a natural number n, you have been tasked to implement
    a function that returns a list of all words from string s that contain exactly
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    selectWords("Mary had a little lamb", 4) ==> ["little"]
    selectWords("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    selectWords("simple white space", 2) ==> []
    selectWords("Hello world", 4) ==> ["world"]
    selectWords("Uncle sam", 3) ==> ["Uncle"]
     */
    public List<String> selectWords(String s, int n) {
        List<String> result = new ArrayList<String>();
        String[] words = s.split(" ");
        for(int i = 0; i < words.length; i++) {
            String word = words[i];
            if(word.length() == n && !isVowel(word)) {
                result.add(word);
            }
        }
        return result;
    }
    private boolean isVowel(String word) {
        for(int i = 0; i < word.length(); i++) {
            if(!Character.isLetter(word.charAt(i)) || "aeiou".indexOf(word.charAt(i)) == -1) {
                return false;
            }
        }
        return true;
    }
}