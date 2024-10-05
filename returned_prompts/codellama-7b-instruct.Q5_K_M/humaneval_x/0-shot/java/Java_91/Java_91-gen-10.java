import java.util.*;

class Solution {
    public int isBored(String S) {
        int count = 0;
        for (String sentence : S.split("[.?!]")) {
            if (sentence.startsWith("I")) {
                count++;
            }
        }
        return count;
    }
}
