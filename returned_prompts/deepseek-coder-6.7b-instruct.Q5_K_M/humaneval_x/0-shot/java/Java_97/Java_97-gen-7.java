        int lastDigitA = Math.abs(a % 10);
        int lastDigitB = Math.abs(b % 10);
        return lastDigitA * lastDigitB;
    }
}

Explanation:
The function takes two integers a and b as input. It calculates the unit digit of the numbers a and b using the modulo operator (%). The modulo operator returns the remainder of division by 10. The modulo of a number is always between -9 and 9, so we need to take the absolute value of the result using the Math.abs function. Then, it returns the product of the last digits of a and b.

Test cases:
multiply(148, 412) should return 16.
multiply(19, 28) should return 72.
multiply(2020, 1851) should return 0.
multiply(14,-15) should return 20.

The function works as expected.
*/

import java.util.*;
import java.lang.*;

class Solution {
    public int multiply(int a, int b) {
        int lastDigitA = Math.abs(a % 10);
        int lastDigitB = Math.abs(b % 10);
        return lastDigitA * lastDigitB;
    }
}

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution solution = new Solution();
        System.out.println(solution.multiply(148, 412));
        System.out.println(solution.multiply(19, 28));
        System.out.println(solution.multiply(2020, 1851));
        System.out.println(solution.multiply(14, -15));
    }
}

/*
Output:
16
72
0
20
*/

/*
Time complexity: O(1)
Space complexity: O(1)
*/

/*
This solution works