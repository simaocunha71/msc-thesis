import java.util.*;
import java.lang.*;

class Solution {
    /**
    Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and true/false for the check.
    Example
    For s = "abcde", c = "ae", the result should be ("bcd",false)
    For s = "abcdef", c = "b"  the result should be ("acdef",false)
    For s = "abcdedcba", c = "ab", the result should be ("cdedc",true)
     */
    public List<Object> reverseDelete(String s, String c) {
        List<Object> result = new ArrayList<>();
        StringBuffer resultString = new StringBuffer();
        for (int i = s.length() - 1; i >= 0; i--) {
            if (c.indexOf(s.charAt(i)) == -1) {
                resultString.append(s.charAt(i));
            }
        }
        boolean isPalindrome = true;
        for (int i = 0; i < resultString.length() / 2; i++) {
            if (resultString.charAt(i) != resultString.charAt(resultString.length() - i - 1)) {
                isPalindrome = false;
                break;
            }
        }
        result.add(resultString.toString());
        result.add(isPalindrome);
        return result;
    }
}
