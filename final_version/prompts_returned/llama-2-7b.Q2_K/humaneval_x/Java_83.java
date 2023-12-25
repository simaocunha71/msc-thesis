import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
     */
    public int startsOneEnds(int n) {
        if (n < 2 || n > 99) { // invalid range
            throw new IllegalArgumentException("n's range is [1, 99]");
        }
        
        List<Integer> candidates = new ArrayList<>();
        for (int i=0;i<=9;i++)
        {
            String str = Integer.toString(i);
            if (str.startsWith("1") && !candidates.contains(i)) // if 1 at the begging
                candidates.add(i);
            else if (str.endsWith("1")) // if 1 in the ending of string
                candidates.add(i);
        }
        
        return candidates.size();
    }
}