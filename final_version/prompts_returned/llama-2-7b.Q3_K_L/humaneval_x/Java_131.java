import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
     */
    public int digits(int n) {
        //Write your code here
        if (n % 2 == 0 ) return 0;
        String str = new Integer(n).toString();
        HashMap<Integer,Integer> map = new HashMap<>();
        for (int i=str.length()-1;i>=0 ;i--) {
            int d = str.charAt(i) - '0';
            if(d % 2 == 0) continue;
            if(!map.containsKey(d)) map.put(d, 1);
            else map.put(d, map.get(d)+1);
        }
        return map.size()-map.get(1);
    }
}