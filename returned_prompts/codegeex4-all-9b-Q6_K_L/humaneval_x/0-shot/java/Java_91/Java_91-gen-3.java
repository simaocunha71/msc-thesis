import java.util.*;
import java.lang.*;

class Solution {
    public int isBored(String S) {
        int count = 0;
        for (String sentence : S.split("[.?!]")) {
            if (sentence.trim().startsWith("I")) {
                count++;
            }
        }
        return count;
    }
}