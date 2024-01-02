import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    antiShuffle("Hi") returns "Hi"
    antiShuffle("hello") returns "ehllo"
    antiShuffle("Hello World!!!") returns "Hello !!!Wdlor"
     */
    public String antiShuffle(String s) {
        // TODO: Implement this method
        Map<Character, Integer> charIndex = new HashMap<Character, Integer>();
        for (int i=0; i<s.length(); i++) {
            charIndex.put(s.charAt(i), i);
        }
        
        String[] temp = s.split(" ");
        StringBuilder sb = new StringBuilder();
        
        // For each word...
        for (int i=0; i<temp.length; i++) {
            char[] chars = temp[i].toCharArray();
            
            // Go over all characters and index the position of that character in this word...
            // (In case of repeated character, it will always have same value)
            for (int j=0; j<chars.length; j++) {
                int idx = charIndex.get(chars[j]);
                
                // If the index of current character is greater than 1 then we'll add a space and
                // move to next word...
                if (idx == 2) {
                    sb.append(" ");
                    
                    continue;
                }
                
                // else we do nothing but get the ascii value of current character
                sb.append(Integer.toChar(chars[j]).charAt(0));
            }
        }
        
        return (sb.toString());
    }
}
