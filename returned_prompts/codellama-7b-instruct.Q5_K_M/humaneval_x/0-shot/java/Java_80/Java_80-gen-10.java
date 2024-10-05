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

        // check if length is at least 3
        if (s.length() < 3) {
            return false;
        }

        // check if every 3 consecutive letters are distinct
        for (int i = 0; i < s.length() - 2; i++) {
            if (s.substring(i, i + 3).equals(s.substring(i + 1, i + 4))) {
                return false;
            }
        }

        return true;
    }
}
