Here is a Java solution. The idea is to count the number of odd and even numbers in each list. If the total number of odd numbers in both lists is even, it means that it is possible to exchange elements between the two lists to make all the elements of lst1 to be even. Otherwise, it is not possible.

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        int oddCount1 = 0, oddCount2 = 0;
        for (int num : lst1) {
            if (num % 2 != 0) {
                oddCount1++;
            }
        }
        for (int num : lst2) {
            if (num % 2 != 0) {
                oddCount2++;
            }
        }
        return (oddCount1 + oddCount2) % 2 == 0 ? "YES" : "NO";
    }
}
```
This solution has a time complexity of O(n), where n is the total number of elements in the two lists.