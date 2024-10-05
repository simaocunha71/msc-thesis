import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
     */
    public int digits(int n) {
        int product = 1;
        boolean isEven = true;
        while(n > 0) {
            int digit = n % 10;
            if(digit % 2 != 0) {
                product *= digit;
                isEven = false;
            }
            n /= 10;
        }
        if(isEven) {
            return 0;
        }
        return product;
    }
}