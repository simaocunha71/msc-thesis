import java.util.*;
import java.lang.*;

class Solution {
    public String antiShuffle(String s) {
        // Split the string into words
        String[] words = s.split(" ");
        
        // Sort each word
        for (int i = 0; i < words.length; i++) {
            char[] chars = words[i].toCharArray();
            Arrays.sort(chars);
            words[i] = new String(chars);
        }
        
        // Join the words back together
        return String.join(" ", words);
    }
}