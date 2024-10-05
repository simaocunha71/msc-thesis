        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        Set<Character> set = new HashSet<>();
        for (char ch : c.toCharArray()) {
            set.add(ch);
        }
        for (char ch : s.toCharArray()) {
            if (!set.contains(ch)) {
                sb.append(ch);
            }
        }
        result.add(sb.toString());
        result.add(isPalindrome(sb.toString()));
        return result;
    }

    private boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}

//Test
Solution sol = new Solution();
System.out.println(sol.reverseDelete("abcde", "ae")); // should return ["bcd", false]
System.out.println(sol.reverseDelete("abcdef", "b")); // should return ["acdef", false]
System.out.println(sol.reverseDelete("abcdedcba", "ab")); // should return ["cdedc", true]


A: Here's the correct Java code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (!c.contains(String.valueOf(ch))) {
                sb.append(ch);
            }
        }
        result.add(sb.toString());
        result.add(isPalindrome(sb.toString()));
        return result;
    }

    private boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while (i <