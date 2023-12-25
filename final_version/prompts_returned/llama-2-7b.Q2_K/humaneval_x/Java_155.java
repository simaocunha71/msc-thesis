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
        
        if(num == 0){
            return new ArrayList();
            
        }else{
            int evens = 0; // count the even digits
            for (int i=1; i<=9; i++) {
                int temp = (int)(Math.pow((double)num, i)-(int)(Math.pow((double)num, i-1))); // find digit at place of i
                    if ((temp % 10) == 0){ // check even or odd digit
                        evens++;
                }
            }
            
            return new ArrayList();
        }
    }
}