Here is the solution to the problem:

```java
import java.util.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        int evenCount = 0;
        for (int num : lst1) {
            if (num % 2 == 0) {
                evenCount++;
            }
        }
        if (evenCount == lst1.size()) {
            return "YES";
        }
        for (int num : lst2) {
            if (num % 2 == 0) {
                lst1.add(num);
                lst2.remove(num);
                if (isAllEven(lst1)) {
                    return "YES";
                }
                lst1.remove(num);
                lst2.add(num);
            }
        }
        return "NO";
    }

    public boolean isAllEven(List<Integer> lst) {
        for (int num : lst) {
            if (num % 2 != 0) {
                return false;
            }
        }
        return true;
    }
}
```

The solution first checks if the number of even numbers in lst1 is equal to the size of lst1. If it is, then it returns "YES". If not, it iterates over lst2 and for each even number in lst2, it adds it to lst1 and removes it from lst2. It then checks if all numbers in lst1 are even. If they are, it returns "YES". If not, it removes the added number from lst1 and adds it back to lst2. If it has iterated over all numbers in lst2 and not found a way to make all numbers in lst1 even, it returns "NO". The isAllEven function checks if all numbers in a list are even. It does this by iterating over the list and returning false as soon as it finds a number that is not even. If it has checked all numbers and not found any that are not even, it returns true.