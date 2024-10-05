Here is the solution for the problem:

```java
import java.util.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        int count = 0;
        for (int num : lst1) {
            if (num % 2 != 0) {
                count++;
            }
        }
        if (count > lst2.size()) {
            return "NO";
        }
        return "YES";
    }
}
```

Explanation:

The solution iterates over the list `lst1` and counts the number of odd numbers. If this count is greater than the size of the list `lst2`, it means that there are more odd numbers in `lst1` than there are elements in `lst2` to exchange, so it's not possible to make `lst1` a list of only even numbers. In this case, the function returns "NO". Otherwise, it returns "YES". This solution assumes that the input lists are non-empty, as stated in the problem description.