```java
import java.util.*;
import java.lang.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        boolean hasOdd = false;
        boolean hasEven = false;
        for (int num : lst1) {
            if (num % 2 == 0) {
                hasEven = true;
            } else {
                hasOdd = true;
            }
        }
        for (int num : lst2) {
            if (num % 2 == 0) {
                hasEven = true;
            } else {
                hasOdd = true;
            }
        }
        if (hasOdd && hasEven) {
            return "YES";
        } else {
            return "NO";
        }
    }
}
```
The above code checks whether there are both odd and even numbers in the lists. If there are, it returns "YES" because it is possible to exchange elements between the two lists to make lst1 a list of only even numbers. If there are no odd numbers in lst1, it returns "NO" because it is not possible to make lst1 a list of only even numbers.