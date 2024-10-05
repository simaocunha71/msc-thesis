import java.util.*;
import java.lang.*;

class Solution {
    /**
    Your task is to implement a function that will simplify the expression
    x * n. The function returns true if x * n evaluates to a whole number and false
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = true
    simplify("1/6", "2/1") = false
    simplify("7/10", "10/2") = false
     */
    public boolean simplify(String x, String n) {
        int gcd = gcd(x, n);
        int xNum = Integer.parseInt(x.split("/")[0]);
        int xDen = Integer.parseInt(x.split("/")[1]);
        int nNum = Integer.parseInt(n.split("/")[0]);
        int nDen = Integer.parseInt(n.split("/")[1]);

        int xMultN = xNum * nNum;
        int nMultX = nDen * xNum;
        int xMultNden = xNum * nDen;
        int nMultXden = nNum * xDen;

        if (gcd == xMultN && gcd == nMultX && gcd == xMultNden && gcd == nMultXden) {
            return true;
        } else {
            return false;
        }
    }

    private int gcd(String x, String n) {
        int xNum = Integer.parseInt(x.split("/")[0]);
        int xDen = Integer.parseInt(x.split("/")[1]);
        int nNum = Integer.parseInt(n.split("/")[0]);
        int nDen = Integer.parseInt(n.split("/")[1]);
        return gcd(xNum, xDen, nNum, nDen);
    }

    private int gcd(int a, int b) {
        if