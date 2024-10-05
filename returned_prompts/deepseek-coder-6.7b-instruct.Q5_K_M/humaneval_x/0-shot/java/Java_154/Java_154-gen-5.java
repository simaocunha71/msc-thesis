        for(int i=0;i<b.length();i++){
            if(a.contains(b)){
                return true;
            }
            b=b.charAt(b.length()-1)+b.substring(0,b.length()-1);
        }
        return false;
    }
}


A: Here is the code that will check for the rotations of the second string in the first string.

```java
import java.util.*;
import java.lang.*;

class Solution  {
    public boolean cycpatternCheck(String a, String b)  {
        if (a.length() < b.length()) {
            return false;
        }
        for (int i = 0; i < b.length(); i++) {
            if (a.contains(b)) {
                return true;
            }
            b = b.charAt(b.length()-1) + b.substring(0, b.length()-1);
        }
        return false;
    }
}
```

This code works by rotating the second string `b` by taking the last character and appending it at the start of the string, then checking if the first string `a` contains the rotated string `b`. If any rotation of `b` is found in `a`, then the method returns `true`. If no rotation of `b` is found in `a` after checking all rotations, the method returns `false`.

Note: If the length of `b` is greater than `a`, it is impossible for `b` to be a substring of `a`, so the method returns `false` in that case.

Test this code with the given examples and it should work as expected.

```java
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.cycpatternCheck("abcd", "abd")); // false
        System.out.println(solution.cycpatternCheck("hello", "ell")); // true
        System.out.println(solution.cycpatternCheck("whassup", "psus")); // false
        System.