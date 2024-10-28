The problem is asking you to add up all the even numbers in the list that have an odd index. 

Here is a simple solution in Java:

```java
import java.util.*;

class Solution {
    public int add(List<Integer> lst) {
        int sum = 0;
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) % 2 == 0) {
                sum += lst.get(i);
            }
        }
        return sum;
    }
}
```

This solution works by iterating over the list and checking each element if it's even (by using the modulus operator `%`). If the element is even, it adds it to the sum. The loop starts from the second element (index 1) because we are looking for elements at odd indices. 

This solution has a time complexity of O(n), where n is the size of the list, because it needs to iterate over the entire list. The space complexity is O(1), because it only uses a constant amount of space to store the sum. 