import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function countNums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> countNums(Arrays.asList()) == 0
    >>> countNums(Arrays.asList(-1, 11, -11)) == 1
    >>> countNums(Arrays.asList(1, 1, 2)) == 3
     */
    public int countNums(List<Integer> arr) {
        if (arr.isEmpty()) return 0;
        
        Set<Integer> temp = new HashSet<>();
        for (int a : arr) {
            long sumDigits = 1L;
            while (a >= 10 && a > 0) {
                a /= 10;
                sumDigits *= 10;
            }
            
            if (sumDigits == 0 || sumDigits % 10 != 0) continue;
            temp.add(a);
        }
        return temp.size();
    }
}