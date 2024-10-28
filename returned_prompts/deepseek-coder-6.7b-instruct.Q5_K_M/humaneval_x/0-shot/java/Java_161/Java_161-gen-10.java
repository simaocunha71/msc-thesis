        String res = "";
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(Character.isLetter(c)){
                if(Character.isUpperCase(c))
                    res += Character.toLowerCase(c);
                else
                    res += Character.toUpperCase(c);
            }else{
                res += c;
            }
        }
        return res;
    }

}


A: You are not correctly implementing the problem statement. It says if s[i] is a letter, reverse its case from lower to upper or vise versa, otherwise keep it as it is. 
In your current implementation, you are reversing the case of each letter in the string, but you are not keeping non-letter characters as they are. 
Here is the correct implementation:
import java.util.*;
import java.lang.*;

class Solution {
    public String solve(String s) {
        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            char c = chars[i];
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    chars[i] = Character.toLowerCase(c);
                } else {
                    chars[i] = Character.toUpperCase(c);
                }
            }
        }
        return new String(chars);
    }
}

This implementation will correctly reverse the case of each letter character in the string, and keep non-letter characters unchanged.

A: You can use Java 8's Stream API to solve this in a more functional style:
import java.util.stream.Collectors;

class Solution {
    public String solve(String s) {
        return s.chars()
            .map(c -> Character.isLetter(c) ? Character.isUpperCase(c) ? Character.toLowerCase(c) : Character.toUpperCase(c) : c)
            .mapToObj(c -> String.valueOf((char)c))
