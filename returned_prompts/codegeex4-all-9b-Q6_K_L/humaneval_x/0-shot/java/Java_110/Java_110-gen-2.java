Here is a Java solution using the `Collections.frequency` method to count the number of even and odd numbers in both lists. If the number of odd numbers in `lst1` is greater than the number of even numbers in `lst2`, it is impossible to make all the elements of `lst1` to be even by exchanging elements between them. Otherwise, it is possible.

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        int oddCount1 = Collections.frequency(lst1, 1);
        int evenCount1 = lst1.size() - oddCount1;
        int oddCount2 = Collections.frequency(lst2, 1);
        int evenCount2 = lst2.size() - oddCount2;
        
        if (oddCount1 > evenCount2) {
            return "NO";
        } else {
            return "YES";
        }
    }
}
```

Please note that this solution assumes that the input lists will be non-empty and the numbers in the lists will be 1 or 2. If the numbers in the lists can be any positive integer, you need to modify the solution to count the number of odd and even numbers correctly.