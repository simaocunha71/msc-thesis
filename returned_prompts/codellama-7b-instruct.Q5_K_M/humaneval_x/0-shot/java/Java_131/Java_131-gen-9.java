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
        // 1 2 3 4 5
        // 0 1 0 1 0
        // 0 0 1 0 0
        // 0 0 0 1 0
        // 0 0 0 0 1
        // 1 2 3 4 5
        // 1 2 3 4 5
        // 0 0 0 1 0
        // 0 0 0 0 1
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0
        // 0 0 0 0 0