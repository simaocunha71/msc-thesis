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

        int numberOfDecimals = 1;
        double decimal = number - (int)number;
        while (numberOfDecimals < 10)
        {
            decimal = number - (int)number;
            if (decimal < 1)
                return decimal;
            numberOfDecimals++;
        }

        return decimal;
    }
}
