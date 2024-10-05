import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
     */
    public int startsOneEnds(int n) {
        int count = 0;
        for (int i = 1; i <= 9; i++) {
            int start = (int) Math.pow(10, n - 2) + i;
            int end = (int) Math.pow(10, n - 1) + i;
            for (int j = start; j <= end; j++) {
                if (j % 10 == 1) {
                    count++;
                }
            }
        }
        return count;
    }
}

