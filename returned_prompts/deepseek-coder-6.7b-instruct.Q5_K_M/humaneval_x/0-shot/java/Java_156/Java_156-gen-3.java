        String[] symbols = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        StringBuilder res = new StringBuilder();

        for (int i = 0; i < values.length && number > 0; i++) {
            while (values[i] <= number) {
                number -= values[i];
                res.append(symbols[i]);
            }
        }

        return res.toString();
    }
}


A: Here is the correct code:

import java.util.*;
import java.lang.*;

class Solution  {
    public String intToMiniRoman(int num) {

        String[] symbols = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        StringBuilder res = new StringBuilder();

        for (int i = 0; i < values.length && num > 0; i++) {
            while (values[i] <= num) {
                num -= values[i];
                res.append(symbols[i]);
            }
        }

        return res.toString();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.intToMiniRoman(19));  // Outputs "xix"
        System.out.println(s.intToMiniRoman(152)); // Outputs "clii"
        System.out