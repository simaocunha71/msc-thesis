import java.util.*;
import java.lang.*;

class Solution {
    /**
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> stringXor("010", "110")
    "100"
     */
    public String stringXor(String a, String b) {

        // StringBuffer is a mutable string class
        StringBuffer sb = new StringBuffer();

        // Iterate over the length of the shorter string
        // This ensures that we do not get IndexOutOfBoundsException
        // while accessing the characters of the strings
        int minLen = Math.min(a.length(), b.length());

        // Iterate over the length of the shorter string
        for (int i = 0; i < minLen; i++) {
            // Perform binary XOR on the characters of the strings
            sb.append((a.charAt(i) == b.charAt(i) ? '0' : '1'));
        }

        // If the strings are of different length, we need to append the remaining
        // characters of the longer string.
        // We can use the length() method to get the length of the longer string
        int maxLen = Math.max(a.length(), b.length());
        if (a.length() < b.length()) {
            for (int i = minLen; i < maxLen; i++) {
                sb.append(b.charAt(i));
            }
        } else {
            for (int i = minLen; i < maxLen; i++) {
                sb.append(a.charAt(i));
            }
        }

        // Return the resultant string
        return sb.toString();
    }
}

B:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> stringXor("010", "110")
    "100"
     */