import java.util.*;
import java.lang.*;

class Solution {
    /**
    Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> howManyTimes("", "a")
    0
    >>> howManyTimes("aaa", "a")
    3
    >>> howManyTimes("aaaa", "aa")
    3
     */
    public int howManyTimes(String string, String substring) {
        int count = 0;
        int i = 0;
        while (i <= string.length() - substring.length()) {
            if (string.substring(i, i + substring.length()).equals(substring)) {
                count++;
                i += substring.length();
            } else {
                i++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.howManyTimes("", "a"));
        System.out.println(s.howManyTimes("aaa", "a"));
        System.out.println(s.howManyTimes("aaaa", "aa"));
    }




