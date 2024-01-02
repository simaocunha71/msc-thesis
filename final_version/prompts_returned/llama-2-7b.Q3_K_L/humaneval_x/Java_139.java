import java.util.*;
import java.lang.*;

class Solution {
    /**
    The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> specialFactorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
     */
    public long specialFactorial(int n) {
        if (n == 0 || n < 0) {
            return 0;
        }
        
        // base cases
        int i=1;
        long currentFactorial = 1;
        while (i<n){
            i++;
            currentFactorial *= i;
            
        }
        currentFactorial -= 1;
        return currentFactorial;
    }
}