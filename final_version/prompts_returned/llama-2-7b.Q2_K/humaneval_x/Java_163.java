import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generateIntegers(2, 8) => [2, 4, 6, 8]
    generateIntegers(8, 2) => [2, 4, 6, 8]
    generateIntegers(10, 14) => []
     */
    public List<Integer> generateIntegers(int a, int b) {
        List<Integer> evenDigits = new ArrayList<>();
        
        Integer mid = (a + b)/2;
         
        if (a > mid){
            int low = a - mid;
            
            for (int i = 0; i <= low; i++) {
                evenDigits.add(Integer.valueOf(i));
            }
        }else{
            int high = b + mid;
             
            for (int j = 0 ; j <= high; j++) {
                Integer num = Integer.valueOf(j);
                
                if (!evenDigits.contains(num)){
                    evenDigits.add(num);
                }
            }            
        }
        
        return evenDigits;
    }
}