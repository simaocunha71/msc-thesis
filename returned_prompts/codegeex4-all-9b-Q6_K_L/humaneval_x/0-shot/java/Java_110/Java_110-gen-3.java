Here is a Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        int oddCount1 = 0;
        int oddCount2 = 0;

        // Count the number of odd numbers in lst1 and lst2
        for (int num : lst1) {
            if (num % 2 != 0) oddCount1++;
        }
        for (int num : lst2) {
            if (num % 2 != 0) oddCount2++;
        }

        // If the number of odd numbers in lst1 is less than or equal to the number of odd numbers in lst2, return "YES"
        if (oddCount1 <= oddCount2) return "YES";
        // Otherwise, return "NO"
        else return "NO";
    }
}
```

The idea of this solution is to count the number of odd numbers in both lists. If the number of odd numbers in lst1 is less than or equal to the number of odd numbers in lst2, we can always exchange enough odd numbers from lst1 to lst2 to make all the elements in lst1 even. Otherwise, it is impossible to make all the elements in lst1 even by exchanging elements between lst1 and lst2.