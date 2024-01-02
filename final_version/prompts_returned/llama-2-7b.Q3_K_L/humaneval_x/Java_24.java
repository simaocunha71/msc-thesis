import java.util.*;
import java.lang.*;

class Solution {
    /**
    For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largestDivisor(15)
    5
     */
    public int largestDivisor(int n) {
        //Write your code here
        int max = 0;
        
       for (int i=2; i<n;i++){//start with the second number which is 2 and keep going until the number becomes bigger than the number you are checking.
        if(n%i == 0){ //if i is a divisor of n then we have found our max, if it isnt go to next iteration.
            max = Math.min(max, i);//if the current i is larger than the previous one save it as maximum
            
        }
        
       } 
        return max;
    }
}