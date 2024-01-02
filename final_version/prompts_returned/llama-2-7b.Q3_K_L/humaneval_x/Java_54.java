import java.util.*;
import java.lang.*;

class Solution {
    /**
    Check if two words have the same characters.
    >>> sameChars("eabcdzzzz", "dddzzzzzzzddeddabc")
    true
    >>> sameChars("abcd", "dddddddabc")
    true
    >>> sameChars("dddddddabc", "abcd")
    true
    >>> sameChars("eabcd", "dddddddabc")
    false
    >>> sameChars("abcd", "dddddddabce")
    false
    >>> sameChars("eabcdzzzz", "dddzzzzzzzddddabc")
    false
     */
    public boolean sameChars(String s0, String s1) {
        if (s0.length() != s1.length()) return false;
        
        Set<Character> set = new HashSet<>();  // TODO: Make this a static class
        
        for (int i=0 ; i<s0.length();i++) {
            char c0 = s0.charAt(i);
            char c1 = s1.charAt(i);
            
            if (!set.contains(c0) || !set.contains(c1)) 
                set.add(c0), set.add(c1);
        }
        
        return set.size() == 2;
    }
}