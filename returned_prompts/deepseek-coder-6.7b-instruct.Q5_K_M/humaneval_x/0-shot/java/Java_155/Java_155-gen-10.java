import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given an integer. return a tuple that has the number of even and odd digits respectively.
    
     Example:
        evenOddCount(-12) ==> 返回 (1, 1)
        evenOddCount(123) ==> 返回 (1, 2)
      */
    public List<Integer> evenOddCount(int num) {
        List<Integer> list = new ArrayList<Integer>();
        int even = 0;
        int odd = 0;
        num = Math.abs(num);
        while(num > 0) {
            int digit = num % 10;
            if(digit % 2 == 0) {
                even++;
            } else {
                odd++;
            }
            num = num / 10;
        }
        list.add(even);
        list.add(odd);
        return list;
    }
}

