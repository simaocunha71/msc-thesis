import java.util.*;
import java.lang.*;

class Solution {
    public int digits(int n) {
        int product = 1;
        boolean hasOdd = false;
        while (n > 0) {
            int digit = n % 10;
            if (digit % 2 != 0) {
                product *= digit;
                hasOdd = true;
            }
            n /= 10;
        }
        return hasOdd ? product : 0;
    }
}