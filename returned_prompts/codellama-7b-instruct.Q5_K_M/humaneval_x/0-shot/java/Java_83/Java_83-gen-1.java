import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
     */
    public int startsOneEnds(int n) {
        int count = 0;
        for (int i = 1; i < (int)Math.pow(10, n); i++) {
            String num = i + "";
            if (num.startsWith("1") || num.endsWith("1")) {
                count++;
            }
        }
        return count;
    }
}
