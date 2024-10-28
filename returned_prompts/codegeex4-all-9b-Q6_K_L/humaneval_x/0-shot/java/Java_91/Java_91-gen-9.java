import java.util.*;
import java.lang.*;

class Solution {
    public int isBored(String S) {
        if (S == null || S.isEmpty()) {
            return 0;
        }

        String[] sentences = S.split("[.?!]");
        int count = 0;
        for (String sentence : sentences) {
            if (sentence.trim().startsWith("I")) {
                count++;
            }
        }
        return count;
    }
}