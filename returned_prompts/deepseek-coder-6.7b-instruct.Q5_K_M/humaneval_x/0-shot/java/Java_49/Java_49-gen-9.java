        if (n == 0) {
            return 1;
        } else {
            int result = 1;
            for(int i = 0; i < n; i++) {
                result = (result * 2) % p;
            }
            return result;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.modp(3, 5));
        System.out.println(solution.modp(1101, 101));
        System.out.println(solution.modp(0, 101));
        System.out.println(solution.modp(3, 11));
        System.out.println(solution.modp(100, 101));
    }
}


A: The problem is with the line of code
result = result * 2 % p;

It should be
result = (result * 2) % p;

The parentheses are missing and you were getting wrong results because of this.
The corrected code is as follows:
import java.util.*;
import java.lang.*;

class Solution  {
    /**
    Return 2^n modulo p  (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
      */
    public int modp(int n, int p)  {

        if (n == 0) {
            return 1;
        } else {
            int result = 1;
            for(int i = 0; i < n; i++) {
                result = (result * 2) % p;
            }
            return result;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.