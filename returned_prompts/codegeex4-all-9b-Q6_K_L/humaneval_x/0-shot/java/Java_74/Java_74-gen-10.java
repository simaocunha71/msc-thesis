```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        int count1 = 0;
        int count2 = 0;
        for (String s : lst1) {
            count1 += s.length();
        }
        for (String s : lst2) {
            count2 += s.length();
        }
        if (count1 <= count2) {
            return lst1;
        } else {
            return lst2;
        }
    }
}
```