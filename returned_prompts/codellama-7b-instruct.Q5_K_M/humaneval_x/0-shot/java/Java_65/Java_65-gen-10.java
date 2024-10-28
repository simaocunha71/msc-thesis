import java.util.*;
import java.lang.*;

class Solution {
    /**
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circularShift(12, 1)
    "21"
    >>> circularShift(12, 2)
    "12"
     */
    public String circularShift(int x, int shift) {

        int digits = (int) (Math.log10(x) + 1);
        if (shift > digits) {
            shift = digits;
        }
        String str = Integer.toString(x);
        String result = "";
        for (int i = 0; i < shift; i++) {
            result += str.charAt(digits - i - 1);
        }
        for (int i = shift; i < digits; i++) {
            result += str.charAt(i);
        }
        return result;
    }

    /**
    Given an array of integers, return a new array such that each element at
    index i of the new array is the product of all the numbers in the original
    array except the one at i.
    For example, if our input was [1, 2, 3, 4, 5], the expected output would be
    [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
    [2, 3, 6].
    Follow-up: what if you can't use division?
    >>> getProduct(new int[] {1, 2, 3, 4, 5})
    [120, 60, 40, 30, 24]
    >>> getProduct(new int[] {1, 2, 3, 4})
    [24, 12, 8, 6]
    >>> getProduct(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 1