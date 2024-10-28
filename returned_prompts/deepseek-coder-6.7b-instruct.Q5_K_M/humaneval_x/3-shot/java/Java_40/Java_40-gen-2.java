        int n = l.size();
        if (n < 3)
            return false;

        Collections.sort(l);

        for (int i = 0; i < n - 1; i++) {
            int a = l.get(i);
            int start = i + 1;
            int end = n - 1;
            while (start < end) {
                if (a + l.get(start) + l.get(end) == 0) {
                    return true;
                } else if (a + l.get(start) + l.get(end) < 0) {
                    start += 1;
                } else {
                    end -= 1;
                }
            }
        }
        return false;
    }
}


A: You can use the following code to solve your problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    triplesSumToZero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triplesSumToZero(Arrays.asList(1, 3, 5, 0))
    false
    >>> triplesSumToZero(Arrays.asList(1, 3, -2, 1))
    true
    >>> triplesSumToZero(Arrays.asList(1, 2, 3, 7))
    false
    >>> triplesSumToZero(Arrays.asList(2, 4, -5, 3, 9, 7))
    true
    >>> triplesSumToZero(Arrays.asList(1))
    false
      */
    public boolean triplesSumToZero(List<Integer> l) {
        int n = l.size();
        if (n < 3)
            return false;

        Collections.sort(l);

        for (int i = 0; i < n - 1; i++) {
            int a = l.get(i);
            int start = i + 1;
            int end = n - 1;
            while