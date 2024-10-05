Here is the Java code for the problem:

```java
import java.util.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        List<Integer> lst1Copy = new ArrayList<Integer>(lst1);
        List<Integer> lst2Copy = new ArrayList<Integer>(lst2);

        for (int i = 0; i < lst1.size(); i++) {
            if (lst1Copy.get(i) % 2 != 0) {
                for (int j = 0; j < lst2.size(); j++) {
                    if (lst2Copy.get(j) % 2 == 0) {
                        lst1Copy.set(i, lst2Copy.get(j));
                        lst2Copy.set(j, lst1Copy.get(i));
                        break;
                    }
                }
            }
        }

        for (int num : lst1Copy) {
            if (num % 2 != 0) {
                return "NO";
            }
        }

        return "YES";
    }
}
```
This solution creates copies of the input lists and then iterates over the first list. For each number in the first list that is not even, it tries to find an even number in the second list and swaps them. If it can't find an even number in the second list, it returns "NO". If it can make all numbers in the first list even, it returns "YES".