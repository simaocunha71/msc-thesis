import java.util.*;
import java.lang.*;

class Solution {
    public Object splitWords(String txt) {
        String[] words = txt.split(" ");
        if (words.length > 1) {
            return words;
        }
        words = txt.split(",");
        if (words.length > 1) {
            return words;
        }
        int count = 0;
        for (char c : txt.toCharArray()) {
            if (Character.isLowerCase(c) && (c - 'a') % 2 != 0) {
                count++;
            }
        }
        return count;
    }
}