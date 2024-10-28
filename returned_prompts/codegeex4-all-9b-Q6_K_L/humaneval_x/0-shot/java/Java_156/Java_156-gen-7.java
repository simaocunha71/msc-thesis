import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> intToMiniRoman(19) == "xix"
    >>> intToMiniRoman(152) == "clii"
    >>> intToMiniRoman(426) == "cdxxvi"
     */
    public String intToMiniRoman(int number) {
        String[] romans = {"i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "xc", "c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "cm", "m", "mm", "mmm"};
        int[] ints = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000};
        String ans = "";
        for(int i = ints.length - 1; i >= 0; i--) {
            while(number - ints[i] >= 0) {
                ans += romans[i];
                number -= ints[i];
            }
        }
        return ans;
    }
}