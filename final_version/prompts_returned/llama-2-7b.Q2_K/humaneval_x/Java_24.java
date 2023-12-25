import java.util.*;
import java.lang.*;

class Solution {
    /**
    For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largestDivisor(15)
    5
     */
    public int largestDivisor(int n) {
        // your code here
        int maxDiv = 1;

        while (n > 0){
            if ((n%maxDiv == 0) && (n%maxDiv < n)){
                break;
            } else{
                maxDiv++;
            }
        }

        return maxDiv;
    }
}
