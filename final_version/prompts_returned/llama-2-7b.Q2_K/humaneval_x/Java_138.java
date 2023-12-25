import java.util.*;
import java.lang.*;

class Solution {
    /**
    Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    isEqualToSumEven(4) == false
    isEqualToSumEven(6) == false
    isEqualToSumEven(8) == true
     */
    public boolean isEqualToSumEven(int n) {
        //Write your code here
        int sum = 0;
        //add even numbers to sum variable
         for (int i : new RangeIntGenerator(n, 4)) {
             sum += i;
         }
        return n == sum + sum + sum + sum;   // n must be divided by 4
    }
}
