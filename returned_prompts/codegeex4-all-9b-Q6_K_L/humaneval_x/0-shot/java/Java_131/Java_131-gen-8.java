import java.util.*;
import java.lang.*;

class Solution {
    public int digits(int n) {
        int product = 1;
        boolean allEven = true;

        while (n > 0) {
            int digit = n % 10;
            if (digit % 2 != 0) {
                product *= digit;
                allEven = false;
            }
            n /= 10;
        }

        return allEven ? 0 : product;
    }
}