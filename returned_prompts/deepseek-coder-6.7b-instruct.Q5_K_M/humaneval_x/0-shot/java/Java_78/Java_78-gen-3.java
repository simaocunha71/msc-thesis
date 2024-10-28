        int count = 0;
        String hex = num.toUpperCase();
        for (int i = 0; i < hex.length(); i++) {
            char c = hex.charAt(i);
            if (c == '2' || c == '3' || c == '5' || c == '7' || c == 'B' || c == 'D') {
                count++;
            }
        }
        return count;
    }

B:
    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();

        System.out.println(s.hexKey("AB")); // 1
        System.out.println(s.hexKey("1077E")); // 2
        System.out.println(s.hexKey("ABED1A33")); // 4
        System.out.println(s.hexKey("123456789ABCDEF0")); // 6
        System.out.println(s.hexKey("2020")); // 2
    }
}
*/

import java.util.*;
import java.lang.*;

class Solution {
    public int hexKey(String num) {
        int count = 0;
        String hex = num.toUpperCase();
        for (int i = 0; i < hex.length(); i++) {
            char c = hex.charAt(i);
            if (c == '2' || c == '3' || c == '5' || c == '7' || c == 'B' || c == 'D') {
                count++;
            }
        }
        return count;
    }

    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();

        System.out.println(s.hexKey("AB")); // 1
        System.out.println(s.hexKey("1077E")); // 2
        System.out.println(s.hexKey("ABED1A33")); // 4
        System.out.println(s.hexKey("12345