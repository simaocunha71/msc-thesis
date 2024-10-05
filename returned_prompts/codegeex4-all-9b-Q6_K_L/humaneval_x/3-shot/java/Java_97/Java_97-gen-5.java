
You have a few issues with your code:

The question asks for a method that takes two integers as arguments, but your method takes two doubles. You should change the method signature to:
public int multiply(int a, int b)

You should not use the magic number 10 in your code. Instead, you should use a constant, which will make your code more readable and easier to maintain. For example:
private static final int UNIT_DIGIT_MODULO = 10;

You should check that the arguments are not negative before performing the calculation. If either of the arguments is negative, the result will always be zero, regardless of the values of the arguments. For example:
public int multiply(int a, int b) {
    if (a < 0 || b < 0) {
        return 0;
    }
    return (a % UNIT_DIGIT_MODULO) * (b % UNIT_DIGIT_MODULO);
}

You should add a comment to explain what the method does. This will make your code more understandable to other developers who may read it in the future. For example:
/**
 * Multiplies the unit digits of two integers.
 *
 * @param a the first integer
 * @param b the second integer
 * @return the product of the unit digits of a and b
 */
public int multiply(int a, int b) {
    if (a < 0 || b < 0) {
        return 0;
    }
    return (a % UNIT_DIGIT_MODULO) * (b % UNIT_DIGIT_MODULO);
}

Here is the corrected version of your code:
import java.util.*;
import java.lang.*;

class Solution {
    private static final int UNIT_DIGIT_MODULO = 10;

    /**
     * Multiplies the unit digits of two integers.
     *
     * @param a the first integer
     * @param b the second integer
     * @return the product of the unit digits of a and b
     */
    public int multiply(int a, int b) {
        if (a < 0 || b < 0) {
            return 0;
        }
        return (a % UNIT_DIGIT_MODULO) * (b % UNIT_DIGIT_MODULO);
    }
}