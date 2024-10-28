import java.util.*;
import java.lang.*;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        Solution ob = new Solution();
        boolean ans = ob.isHappy(s);
        System.out.println(ans ? "Yes" : "No");
    }

    public boolean isHappy(String s) {
        // Write your code here
        int len = s.length();
        if (len < 3) return false;
        for (int i = 0; i < len - 2; i++) {
            if (s.charAt(i) == s.charAt(i + 1) && s.charAt(i + 1) == s.charAt(i + 2)) {
                return false;
            }
        }
        return true;
    }
}
