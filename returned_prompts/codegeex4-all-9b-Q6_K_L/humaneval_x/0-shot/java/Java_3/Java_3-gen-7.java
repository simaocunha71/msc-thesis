```java
import java.util.*;
import java.lang.*;

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
- Initialize the balance to 0.
- Iterate through the operations list.
- For each operation, add it to the balance.
- If the balance becomes negative, return true.
- If the loop completes without the balance becoming negative, return false.