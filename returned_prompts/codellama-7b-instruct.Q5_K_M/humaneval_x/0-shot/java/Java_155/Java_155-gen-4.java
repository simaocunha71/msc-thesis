import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given an integer. return a tuple that has the number of even and odd digits respectively.
    
     Example:
        evenOddCount(-12) ==> (1, 1)
        evenOddCount(123) ==> (1, 2)
     */
    public List<Integer> evenOddCount(int num) {
        List<Integer> result = new ArrayList<>();
        int count = 0;
        for (int i = 0; i < num.length(); i++) {
            if (num.charAt(i) % 2 == 0)
                count++;
        }
        result.add(count);
        result.add(num.length() - count);
        return result;
    }
}