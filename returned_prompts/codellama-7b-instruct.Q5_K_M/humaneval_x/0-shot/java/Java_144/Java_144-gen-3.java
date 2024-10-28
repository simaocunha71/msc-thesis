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
        int numeratorX = Integer.parseInt(x.split("/")[0]);
        int denominatorX = Integer.parseInt(x.split("/")[1]);
        int numeratorN = Integer.parseInt(n.split("/")[0]);
        int denominatorN = Integer.parseInt(n.split("/")[1]);

        int gcd = gcd(numeratorX, denominatorX);
        int gcdN = gcd(numeratorN, denominatorN);

        numeratorX /= gcd;
        denominatorX /= gcd;
        numeratorN /= gcdN;
        denominatorN /= gcdN;

        if(numeratorX * denominatorN == numeratorN * denominatorX) {
            return true;
        } else {
            return false;
        }
    }

    private int gcd(int a, int b) {
        if(a == 0) {
            return b;
        }
        return gcd(b % a, a);
    }
}
