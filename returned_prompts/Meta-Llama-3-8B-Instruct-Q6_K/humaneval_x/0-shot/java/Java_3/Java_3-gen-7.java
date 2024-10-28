Here is the solution for the problem. The idea is to iterate over the list of operations and check if the balance ever falls below zero. If it does, return True, otherwise return False.

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

This solution has a time complexity of O(n), where n is the number of operations, because it needs to iterate over the list of operations once. The space complexity is O(1), because it only uses a constant amount of space to store the balance. 

The unit tests you provided are correct. The first one will return False because the balance never falls below zero. The second one will return True because the balance falls below zero after the third operation. 

You can use the following code to run the unit tests:

```java
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.belowZero(Arrays.asList(1, 2, 3))); // False
        System.out.println(solution.belowZero(Arrays.asList(1, 2, -4, 5))); // True
    }
}
```  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  } 