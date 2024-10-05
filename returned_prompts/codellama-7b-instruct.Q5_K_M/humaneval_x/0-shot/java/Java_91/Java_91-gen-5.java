import java.util.*;

class Solution {
    public int isBored(String S) {
        int count = 0;
        String[] splitSentences = S.split("[.?!]");
        for (String sentence : splitSentences) {
            if (sentence.startsWith("I")) {
                count++;
            }
        }
        return count;
    }
}
