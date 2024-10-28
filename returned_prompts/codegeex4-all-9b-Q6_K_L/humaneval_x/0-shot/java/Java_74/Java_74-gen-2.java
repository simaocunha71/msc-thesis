```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        int sum1 = 0;
        for (String s : lst1) {
            sum1 += s.length();
        }
        int sum2 = 0;
        for (String s : lst2) {
            sum2 += s.length();
        }
        if (sum1 < sum2) {
            return lst1;
        } else if (sum1 > sum2) {
            return lst2;
        } else {
            return lst1;
        }
    }
}
```