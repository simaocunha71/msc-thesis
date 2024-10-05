        if (s.length() < 3) {
            return false;
        }

        for (int i = 0; i < s.length() - 2; i++) {
            if (s.charAt(i) == s.charAt(i+1) || s.charAt(i+1) == s.charAt(i+2) || s.charAt(i) == s.charAt(i+2)) {
                return false;
            }
        }

        return true;
    }
}

I'm not sure if you have a specific rule for when a string is considered happy, but this solution checks each group of three characters to see if they are all distinct. If they are, the string is considered happy.
*/

import java.util.*;
import java.lang.*;

class Solution {
    public static boolean isHappy(String s) {
        if (s.length() < 3) {
            return false;
        }

        for (int i = 0; i < s.length() - 2; i++) {
            if (s.charAt(i) == s.charAt(i+1) || s.charAt(i+1) == s.charAt(i+2) || s.charAt(i) == s.charAt(i+2)) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println(isHappy("a")); // false
        System.out.println(isHappy("aa")); // false
        System.out.println(isHappy("abcd")); // true
        System.out.println(isHappy("aabb")); // false
        System.out.println(isHappy("adb")); // true
        System.out.println(isHappy("xyy")); // false
    }
}

/*
This solution checks each group of three characters in the string to see if they are all distinct. If they are, the string is considered happy and the method returns true. If any two characters are the same or if any two characters are the same