import java.util.*;
import java.lang.*;

class Solution {
    /**
    Complete the function that takes two integers and returns
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
     */
    public int multiply(int a, int b) {

        int a1 = a % 10, a2 = a / 10 % 10, a3 = a / 100;
        int b1 = b % 10, b2 = b / 10 % 10, b3 = b / 100;

        int c1 = a1 * b1, c2 = a2 * b2, c3 = a3 * b3;
        int c4 = a1 * b2 + a2 * b1;
        int c5 = a1 * b3 + a3 * b1;
        int c6 = a2 * b3 + a3 * b2;

        int d1 = c1 + c2 + c4;
        int d2 = c3 + c4 + c5;
        int d3 = c5 + c6;

        return d1 * 100 + d2 * 10 + d3;
    }
}