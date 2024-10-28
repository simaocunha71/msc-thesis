        int sum = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isUpperCase(c)) {
                sum += (int) c;
            }
        }
        return sum;
    }
}

This solution works by iterating over the string and checking if each character is uppercase. If it is, the ASCII value of the character is added to the sum.
*/

// This solution is correct.

import java.util.*;
import java.lang.*;

class Solution {
    public int digitSum(String s) {
        int sum = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isUpperCase(c)) {
                sum += (int) c;
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.digitSum("abAB"));  // 131
        System.out.println(sol.digitSum("abcCd"));  // 67
        System.out.println(sol.digitSum("helloE"));  // 69
        System.out.println(sol.digitSum("woArBld"));  // 131
        System.out.println(sol.digitSum("aAaaaXa"));  // 153
    }
}

/*
The time complexity of the solution is O(n), where n is the length of the string. This is because we are iterating over the string once. 

The space complexity of the solution is O(1), as we are not using any additional space that scales with the size of the input.
*/

// This solution is correct.

import java.util.*;
import java.lang.*;

class Solution {
    public int digitSum(String s) {
        int sum = 0;

        for (int i = 0; i < s.length(); i++) {