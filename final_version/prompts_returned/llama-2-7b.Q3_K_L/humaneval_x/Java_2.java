import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncateNumber(3.5)
    0.5
     */
    public double truncateNumber(double number) {
        BigInteger b = new BigInteger(String.valueOf(number)); // convert given float to string
        int i1 = (int)(Math.floor(b.divide(new BigInteger("10000")))); // get the integer part of the input
        int decimals = (i1 / 10) - i1; // get the number of decimals
        double res = (number-i1)/decimals; // get the decimal part and multiply by 10 to convert it to double
        return Math.round(res*10)+"."+Math.round((res/10));
    }
}