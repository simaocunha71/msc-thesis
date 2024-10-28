        List<Object> result = new ArrayList<>();
        Set<Character> set = new HashSet<>();
        for(char ch:c.toCharArray()){
            set.add(ch);
        }
        StringBuilder sb = new StringBuilder();
        for(char ch:s.toCharArray()){
            if(!set.contains(ch)){
                sb.append(ch);
            }
        }
        String str = sb.toString();
        boolean isPalindrome = str.equals(new StringBuilder(str).reverse().toString());
        result.add(str);
        result.add(isPalindrome);
        return result;
    }
}

*/

import java.util.*;
import java.lang.*;

class Solution  {
    public List<Object> reverseDelete(String s, String c)  {
        List<Object> result = new ArrayList<>();
        Set<Character> set = new HashSet<>();
        for(char ch:c.toCharArray()){
            set.add(ch);
        }
        StringBuilder sb = new StringBuilder();
        for(char ch:s.toCharArray()){
            if(!set.contains(ch)){
                sb.append(ch);
            }
        }
        String str = sb.toString();
        boolean isPalindrome = str.equals(new StringBuilder(str).reverse().toString());
        result.add(str);
        result.add(isPalindrome);
        return result;
    }
}

class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution sol = new Solution();
        System.out.println(sol.reverseDelete("abcde", "ae")); // returns: [bcd, false]
        System.out.println(sol.reverseDelete("abcdef", "b"));  // returns: [acdef, false]
        System.out.println(sol.reverseDelete("abcdedcba", "ab")); // returns: [cdedc, true]
    }
}