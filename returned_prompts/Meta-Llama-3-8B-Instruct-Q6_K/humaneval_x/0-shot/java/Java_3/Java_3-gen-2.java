Here is the solution:

```java
import java.util.*;

class Solution {
    public boolean belowZero(List<Integer> operations) {
        int balance = 0;
        for (int operation : operations) {
            balance += operation;
            if (balance < 0) {
                return true;
            }
        }
        return false;
    }
}
```

Explanation: 
This problem can be solved by iterating over the list of operations and updating the balance accordingly. If at any point the balance falls below zero, we return true. If we finish iterating over the list and the balance is still non-negative, we return false. 

The time complexity of this solution is O(n), where n is the number of operations, as we need to iterate over the list of operations once. The space complexity is O(1), as we only use a constant amount of space to store the balance. 

You can test this solution with the examples you provided:

```java
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> operations1 = Arrays.asList(1, 2, 3);
        List<Integer> operations2 = Arrays.asList(1, 2, -4, 5);
        System.out.println(solution.belowZero(operations1));  // false
        System.out.println(solution.belowZero(operations2));  // true
    }
}
```

This will output:

```
false
true
```  as expected. 