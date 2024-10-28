import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
     */
    public int digitSum(String s) {
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'A' && c <= 'Z') {
                sum += c;
            }
        }
        return sum;
    }

    /**
    Write a function that takes a string as input and returns the sum of the lower characters only'
    ASCII codes.

    Examples:
        letterSum("") => 0
        letterSum("abAB") => 131
        letterSum("abcCd") => 67
        letterSum("helloE") => 69
        letterSum("woArBld") => 131
        letterSum("aAaaaXa") => 153
     */
    public int letterSum(String s) {
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'z') {
                sum += c;
            }
        }
        return sum;
    }

    /**
    Write a function that takes a string as input and returns the sum of the characters only'
    ASCII codes.

    Examples:
        asciiSum("") => 0
        asciiSum("abAB") => 131
        asciiSum("abcCd") => 67
        asciiSum("helloE") => 69
        as