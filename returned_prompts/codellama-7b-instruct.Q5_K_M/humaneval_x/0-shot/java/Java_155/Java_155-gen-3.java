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
        List<Integer> count = new ArrayList<>();
        count.add(0);
        count.add(0);
        while(num != 0){
            if(num % 2 == 0){
                count.set(0, count.get(0) + 1);
            }else{
                count.set(1, count.get(1) + 1);
            }
            num = num / 10;
        }
        return count;
    }
}
