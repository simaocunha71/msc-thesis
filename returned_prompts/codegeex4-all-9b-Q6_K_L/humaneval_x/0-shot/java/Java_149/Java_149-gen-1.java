Here is the solution:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> listSort(List<String> lst) {
        lst.removeIf(s -> s.length() % 2 != 0);
        lst.sort((s1, s2) -> s1.length() == s2.length() ? s1.compareTo(s2) : s1.length() - s2.length());
        return lst;
    }
}
```

Explanation:

1. First, we remove all strings in the list that have odd lengths using the `removeIf` method. The lambda expression `s -> s.length() % 2 != 0` checks if the length of a string is odd.

2. Then, we sort the list using the `sort` method. The lambda expression `(s1, s2) -> s1.length() == s2.length() ? s1.compareTo(s2) : s1.length() - s2.length()` compares two strings based on their lengths. If the lengths are equal, it compares them lexicographically using the `compareTo` method. If the lengths are not equal, it compares them based on their lengths.

3. Finally, we return the sorted list.