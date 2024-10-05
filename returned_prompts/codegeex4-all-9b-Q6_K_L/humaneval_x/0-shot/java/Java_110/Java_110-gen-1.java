To solve this problem, we need to check if there is at least one even number in lst2 and if there is at least one odd number in lst1. If both conditions are met, we can exchange an odd number from lst1 with an even number from lst2 to make all numbers in lst1 even. If either condition is not met, it is not possible to make all numbers in lst1 even by exchanging elements between lst1 and lst2.

Here is the implementation of the exchange function in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        boolean hasEven = false;
        boolean hasOdd = false;

        for (int num : lst2) {
            if (num % 2 == 0) {
                hasEven = true;
                break;
            }
        }

        for (int num : lst1) {
            if (num % 2 != 0) {
                hasOdd = true;
                break;
            }
        }

        if (hasEven && hasOdd) {
            return "YES";
        } else {
            return "NO";
        }
    }
}
```

The exchange function iterates over lst2 to check if there is at least one even number. If an even number is found, the hasEven variable is set to true and the loop is terminated. Similarly, the function iterates over lst1 to check if there is at least one odd number. If an odd number is found, the hasOdd variable is set to true and the loop is terminated.

If both hasEven and hasOdd are true, it means that there is at least one even number in lst2 and at least one odd number in lst1. In this case, it is possible to exchange an odd number from lst1 with an even number from lst2 to make all numbers in lst1 even. Therefore, the function returns "YES". Otherwise, it returns "NO".