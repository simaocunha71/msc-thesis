import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100.
    Example:
    isMultiplyPrime(30) == true
    30 = 2 * 3 * 5
     */
    public boolean isMultiplyPrime(int a) {

        for (int i = 2; i < 100; i++) {
            if (a % i == 0) {
                int j = a / i;
                if (j % i == 0) {
                    int k = j / i;
                    if (k == i) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
