        List<Object> list = new ArrayList<Object>();
        StringBuilder str = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            if(!c.contains(String.valueOf(s.charAt(i)))){
                str.append(s.charAt(i));
            }
        }
        list.add(str.toString());
        list.add(str.toString().equals(str.reverse().toString()));
        return list;
    }
}


A: It seems you are almost there, you have just used the StringBuilder to reverse the string which is not necessary. You can do the palindrome check by comparing the reversed string with the original string. Here is the corrected code:
import java.util.*;
import java.lang.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        List<Object> list = new ArrayList<Object>();
        StringBuilder str = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            if(!c.contains(String.valueOf(s.charAt(i)))){
                str.append(s.charAt(i));
            }
        }
        list.add(str.toString());
        list.add(str.toString().equals(str.reverse().toString()));
        return list;
    }
}

In your code, you have used StringBuilder to reverse the string which is not necessary. The palindrome check can be done by comparing the original string and its reversed version.

A: Here is a simple way to solve it using Java 8 streams:
import java.util.*;
import java.util.stream.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        String result = IntStream.range(0, s.length())
                                 .mapToObj(i -> String.valueOf(s.charAt(i)))
                                 .filter(ch -> !c.contains(ch))
                                 .collect(Collector.of(StringBuilder::new, StringBuilder::append, StringBuilder::append, sb -> sb.toString()));
        return Ar