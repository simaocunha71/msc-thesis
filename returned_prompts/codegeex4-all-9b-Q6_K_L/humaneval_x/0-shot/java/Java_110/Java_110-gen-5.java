```java
import java.util.*;
import java.lang.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        boolean hasOdd = false;
        for (int num : lst1) {
            if (num % 2 != 0) {
                hasOdd = true;
                break;
            }
        }
        if (!hasOdd) {
            return "YES";
        }
        for (int num : lst2) {
            if (num % 2 == 0) {
                return "YES";
            }
        }
        return "NO";
    }
}
```
This solution works by first checking if lst1 contains any odd numbers. If it does, it then checks if lst2 contains any even numbers. If lst1 does not contain any odd numbers, it returns "YES" because lst1 is already a list of only even numbers. If lst2 does not contain any even numbers, it returns "NO" because it is not possible to exchange elements between lst1 and lst2 to make lst1 a list of only even numbers. If lst1 contains odd numbers and lst2 contains even numbers, it returns "YES" because it is possible to exchange elements between lst1 and lst2 to make lst1 a list of only even numbers.