import java.util.*;
import java.lang.*;

class Solution {
    /**
    You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    isHappy(a) => false
    isHappy(aa) => false
    isHappy(abcd) => true
    isHappy(aabb) => false
    isHappy(adb) => true
    isHappy(xyy) => false
     */
    public boolean isHappy(String s) {

        // code here
        int n = s.length();
        if (n < 3) return false;
        for (int i = 0; i <= n - 3; i++) {
            if (s.charAt(i) == s.charAt(i + 1) && s.charAt(i + 1) == s.charAt(i + 2)) return false;
        }
        return true;

    }
}