Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        List<Integer> lst1Copy = new ArrayList<Integer>(lst1);
        for (int i = 0; i < lst1Copy.size(); i++) {
            if (lst1Copy.get(i) % 2 != 0) {
                boolean found = false;
                for (int j = 0; j < lst2.size(); j++) {
                    if (lst2.get(j) % 2 == 0) {
                        lst1Copy.set(i, lst2.get(j));
                        lst2.set(j, lst1Copy.get(i));
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    return "NO";
                }
            }
        }
        return "YES";
    }
}
```

This solution creates a copy of lst1 and then iterates through it. If it finds an odd number, it searches for an even number in lst2 and swaps them. If it can't find an even number in lst2 to swap with the odd number, it returns "NO". If it successfully swaps all the odd numbers in lst1 with even numbers from lst2, it returns "YES". This solution has a time complexity of O(n^2) where n is the size of lst1. This is because in the worst case, it may need to iterate through lst2 for each odd number in lst1. The space complexity is O(n) for the copy of lst1. This is because it needs to store a copy of lst1.