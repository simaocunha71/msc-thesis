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
        if (s == null || s.length() < 1) return result;
        
        Map<Character, List<Character>> charListMap = new HashMap<>();
        for (int i=0;i<c.length();i++) {
            char cFromC = c.charAt(i);
            if (cFromC == '\'') continue;
            
            if (!charListMap.containsKey(cFromC)) {
                List<Character> temp = new ArrayList<>();
                charListMap.put(cFromC,temp);
            } else {
                charListMap.get(cFromC).add(cFromC);
            }
        }
        
        for (int i=0;i<s.length();i++) {
            if (!charListMap.containsKey(s.charAt(i))) continue;
            
            List<Character> temp = charListMap.get(s.charAt(i));
            char cFromS = s.charAt(i);
            for (int j=0;j<temp.size();j++) {
                if (cFromS == '\'') continue;                        
                String tempString = new StringBuilder().append(s.substring(0,i)).append("").toString();
                char cFromTmpStr = temp