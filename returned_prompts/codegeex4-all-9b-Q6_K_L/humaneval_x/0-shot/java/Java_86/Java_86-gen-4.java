```java
import java.util.*;
import java.lang.*;

class Solution {
    public String antiShuffle(String s) {
        if (s == null || s.length() == 0) return s;

        String[] words = s.split(" ");
        StringBuilder sb = new StringBuilder();

        for (String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            sb.append(new String(chars)).append(" ");
        }

        return sb.toString().trim();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.antiShuffle("Hi"));  // "Hi"
        System.out.println(sol.antiShuffle("hello"));  // "ehllo"
        System.out.println(sol.antiShuffle("Hello World!!!"));  // "Hello !!!Wdlor"
    }
}
```