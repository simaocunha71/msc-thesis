        int x = (int)Math.round(Math.cbrt(a));
        return a == x * x * x;
    }
}

Explanation:
The method `iscube` takes an integer `a` as input and returns a boolean value.
It calculates the cube root of `a` and rounds it to the nearest integer using the `Math.round` method. This gives the smallest integer `x` such that `x` is a cube root of `a`.
Then it checks if `a` is equal to `x` cubed. If it is, then `a` is a cube of some integer, and the method returns true. Otherwise, it returns false. 

Test the function:
import java.util.*;
import java.lang.*;

class Test {
    public static void main (String[] args) throws java.lang.Exception {
        Solution sol = new Solution();
        System.out.println(sol.iscube(1)); // true
        System.out.println(sol.iscube(2)); // false
        System.out.println(sol.iscube(-1)); // true
        System.out.println(sol.iscube(64)); // true
        System.out.println(sol.iscube(0)); // true
        System.out.println(sol.iscube(180)); // false
    }
}

Note:
This solution uses the `Math.cbrt` method to calculate the cube root of a number and the `Math.round` method to round the cube root to the nearest integer. This is because `Math.cbrt` returns a double and `Math.round` returns an integer.
The condition `a == x * x * x` checks if `a` is equal to the cube of `x`. If it is, then `a` is a cube of some integer, and the method returns true. Otherwise, it returns false.

The time complexity of this solution is O(1), as it does not depend on the size of the input. The space complexity is also O(1), as it does not use any additional data structures that scale with the size of the input.
*/

// Solution:

// 