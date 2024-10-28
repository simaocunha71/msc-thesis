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
        int unitA = Math.abs(a % 10);
        int unitB = Math.abs(b % 10);
        return unitA * unitB;
    }
}