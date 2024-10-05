```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean cycpatternCheck(String a, String b) {
        Set<String> rotations = new HashSet<>();
        for (int i = 0; i < b.length(); i++) {
            rotations.add(b.substring(i) + b.substring(0, i));
        }
        for (String rotation : rotations) {
            if (a.contains(rotation)) {
                return true;
            }
        }
        return false;
    }
}
```
This solution first generates all possible rotations of the second word and adds them to a set. Then it checks if any of these rotations is a substring of the first word. If it finds a match, it returns true, otherwise it returns false.