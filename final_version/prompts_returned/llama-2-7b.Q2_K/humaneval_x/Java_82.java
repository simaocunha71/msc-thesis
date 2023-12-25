import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that takes a string and returns true if the string
    length is a prime number or false otherwise
    Examples
    primeLength("Hello") == true
    primeLength("abcdcba") == true
    primeLength("kittens") == true
    primeLength("orange") == false
     */
    public boolean primeLength(String string) {
        if (string.length() < 2) return false;
         // Create array of all the numbers that can be
         // divided by all the elements in the string i.e.
         // "Hello".
         int[] nums = new int[10];
         
         for (int j = 2; j < string.length(); j++) {
             if (!(string.indexOf("1" + j) == -1)) {
                 nums[j-1]++;
                 // If the divisor is 0 then return false since it is
                 // not a prime number
                 if (nums[j-1]==0){
                     return false;
                 }
             }
         }
         
         for (int i = 2 ; i <= nums.length; i++) {
            // If the divisor is equal to zero
            // then return false otherwise check if it can divide all
            // elements in the string array and if yes, return true,
            else{
                    if (string.indexOf("1" + String.valueOf(i)) == -1) {return false;}
            
                }
         }
         
        return true;
    }
    
}