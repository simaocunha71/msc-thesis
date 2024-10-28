```java
import java.util.*;
import java.lang.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        // count the number of odd numbers in lst1
        int odd_count = 0;
        for (int num : lst1) {
            if (num % 2 != 0) {
                odd_count++;
            }
        }
        // count the number of even numbers in lst2
        int even_count = 0;
        for (int num : lst2) {
            if (num % 2 == 0) {
                even_count++;
            }
        }
        // if the number of odd numbers in lst1 is less than or equal to the number of even numbers in lst2,
        // then it is possible to exchange elements between them to make all the elements of lst1 to be even
        if (odd_count <= even_count) {
            return "YES";
        } else {
            return "NO";
        }
    }
}
```
The above code first counts the number of odd numbers in lst1 and the number of even numbers in lst2. If the number of odd numbers in lst1 is less than or equal to the number of even numbers in lst2, then it is possible to exchange elements between them to make all the elements of lst1 to be even, so the function returns "YES". Otherwise, the function returns "NO".