import java.util.*;
import java.lang.*;

class Solution {
    /**
    A simple program which should return the value of x if n is
    a prime number and should return the value of y otherwise.

    Examples:
    for xOrY(7, 34, 12) == 34
    for xOrY(15, 8, 5) == 5
     */
    public int xOrY(int n, int x, int y) {
        if (n % x != 0 && n % y != 0 ) return Math.max(x,y);
        if (n % x > 0 && n % x == 1) return n - n % x;
        else return n / y + 2 * y; //return value of x which is evenly divisible by y
    }
}
