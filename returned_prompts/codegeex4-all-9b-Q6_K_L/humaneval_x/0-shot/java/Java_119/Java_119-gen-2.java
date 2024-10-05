```java
import java.util.*;
import java.lang.*;

class Solution {
    public String matchParens(List<String> lst) {
        if (lst.size() != 2) {
            return "No";
        }
        int count1 = 0, count2 = 0;
        for (char c : lst.get(0).toCharArray()) {
            if (c == '(') {
                count1++;
            } else {
                count1--;
            }
        }
        for (char c : lst.get(1).toCharArray()) {
            if (c == ')') {
                count2++;
            } else {
                count2--;
            }
        }
        if (count1 == 0 && count2 == 0) {
            return "Yes";
        } else {
            return "No";
        }
    }
}
```