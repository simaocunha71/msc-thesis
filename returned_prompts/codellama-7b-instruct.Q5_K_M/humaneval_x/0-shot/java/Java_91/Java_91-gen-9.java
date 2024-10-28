import java.util.*;
import java.lang.*;

class Solution {
    public int isBored(String S) {
        int count = 0;
        String[] words = S.split("[.?!]");
        for (String word : words) {
            if (word.equals("I")) {
                count++;
            }
        }
        return count;
    }
}
