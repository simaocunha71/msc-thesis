Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        Set<Integer> evenNumbers = new HashSet<>();
        for (int num : lst2) {
            if (num % 2 == 0) {
                evenNumbers.add(num);
            }
        }
        for (int num : lst1) {
            if (!evenNumbers.contains(num)) {
                return "NO";
            }
            evenNumbers.remove(num);
        }
        return "YES";
    }
}
```

This solution works by first creating a set of all even numbers from the second list. Then, it iterates over the first list, and for each number, it checks if it is not contained in the set of even numbers. If it is not, it immediately returns "NO". If it is, it removes the number from the set. If it finishes iterating over the first list without finding any odd numbers, it returns "YES". This is because it has successfully removed all odd numbers from the first list by exchanging them with even numbers from the second list.