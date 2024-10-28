The problem can be solved by iterating over the elements of lst1 and lst2, 
and keeping track of the count of even numbers in lst1 and lst2. 
If the count of even numbers in lst1 is greater than the count of even numbers 
in lst2, then it is impossible to make all elements of lst1 even by exchanging 
elements with lst2. Otherwise, it is possible to make all elements of lst1 even 
by exchanging elements with lst2.

Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        int evenCount1 = 0, evenCount2 = 0;
        for (int i : lst1) {
            if (i % 2 == 0) {
                evenCount1++;
            }
        }
        for (int i : lst2) {
            if (i % 2 == 0) {
                evenCount2++;
            }
        }
        return evenCount1 > evenCount2 ? "NO" : "YES";
    }
}
```

This solution has a time complexity of O(n), where n is the size of the input lists. 
It iterates over the elements of lst1 and lst2 once to count the number of even numbers. 
The space complexity is O(1), as it uses a constant amount of space to store the count of even numbers. 

For example, if we call `exchange(Arrays.asList(1, 2, 3, 4), Arrays.asList(1, 2, 3, 4))`, 
the function will return "YES", because we can make all elements of lst1 even by exchanging 
elements with lst2. If we call `exchange(Arrays.asList(1, 2, 3, 4), Arrays.asList(1, 5, 3, 4))`, 
the function will return "NO", because we cannot make all elements of lst1 even by exchanging 
elements with lst2. 