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
        List<Integer> res = new ArrayList<>();
        
        while (b > a){
            if((a&1) == 0 && (b & 1)==0){
                res.add(a);
            }else{
                a++;
            }
            
            b--;
        }
    	
        return res;
    }
}