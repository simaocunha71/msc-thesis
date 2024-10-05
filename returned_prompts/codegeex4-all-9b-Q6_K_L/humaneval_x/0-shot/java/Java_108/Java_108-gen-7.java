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
        int count = 0;
        for (int num : arr) {
            int sum = 0;
            if (num < 0) {
                num = -num;
                sum -= 1; // subtract 1 for the negative sign
            }
            while (num > 0) {
                sum += num % 10;
                num /= 10;
            }
            if (sum > 0) {
                count++;
            }
        }
        return count;
    }
}