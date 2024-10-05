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
        result.add(0);
        result.add(0);
        int n = num;
        while (n > 0) {
            if (n % 10 % 2 == 0) {
                result.set(0, result.get(0) + 1);
            } else {
                result.set(1, result.get(1) + 1);
            }
            n = n / 10;
        }
        return result;
    }
}
