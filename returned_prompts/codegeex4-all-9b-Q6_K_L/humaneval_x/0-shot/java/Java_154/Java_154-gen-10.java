```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean cycpatternCheck(String a, String b) {
        // if a is shorter than b, return false
        if (a.length() < b.length()) {
            return false;
        }
        // if b is empty, return true
        if (b.isEmpty()) {
            return true;
        }
        // if a is equal to b, return true
        if (a.equals(b)) {
            return true;
        }
        // if a is longer than b, check if b is a substring of a
        if (a.contains(b)) {
            return true;
        }
        // create a new string with b+b
        String newString = b + b;
        // check if newString is a substring of a
        if (a.contains(newString)) {
            return true;
        }
        // return false
        return false;
    }
}
```
