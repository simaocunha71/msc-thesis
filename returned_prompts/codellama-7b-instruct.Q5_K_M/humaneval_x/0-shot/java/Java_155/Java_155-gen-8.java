import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given an integer. return a tuple that has the number of even and odd digits respectively.
    
     Example:
        evenOddCount(-12) ==> (1, 1)
        evenOddCount(123) ==> (1, 2)
     */
    public List<Integer> evenOddCount(int num) {
        List<Integer> res = new ArrayList<Integer>();
        int countEven = 0;
        int countOdd = 0;
        
        while(num != 0){
            if(num % 10 % 2 == 0)
                countEven += 1;
            else
                countOdd += 1;
            
            num /= 10;
        }
        
        res.add(countEven);
        res.add(countOdd);
        
        return res;
    }
}