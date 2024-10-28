        int increaseCounter = 0;
        int decreaseCounter = 0;

        for (int i = 0; i < l.size() - 1; i++) {
            if (l.get(i) < l.get(i + 1)) {
                increaseCounter++;
            } else if (l.get(i) > l.get(i + 1)) {
                decreaseCounter++;
            }
        }

        return increaseCounter <= 1 || decreaseCounter <= 1;
    }
}


A: The problem was not in the solution, it was in the question itself. The problem statement mentioned that the list can contain duplicates. However, the function only checks for strictly increasing and decreasing sequences.

If you want to also accept lists that are equal (e.g. [1, 2, 2, 4]), you can modify the function to return true if increaseCounter <= 1 and decreaseCounter <= 1:

```java
public boolean monotonic(List<Integer> l) {
    int increaseCounter = 0;
    int decreaseCounter = 0;

    for (int i = 0; i < l.size() - 1; i++) {
        if (l.get(i) < l.get(i + 1)) {
            increaseCounter++;
        } else if (l.get(i) > l.get(i + 1)) {
            decreaseCounter++;
        }
    }

    return increaseCounter <= 1 && decreaseCounter <= 1;
}
```

This way, the function will return true for both increasing and decreasing sequences (even if they are equal), and false otherwise.


A: You can use Java 8's Stream API to simplify the solution. Here is the code:

```java
import java.util.*;
import java.util.stream.*;

class Solution {
    public boolean isMonotonic(List<Integer> list) {
        return IntStream.range(0, list.size() - 1)
            .allMatch(i -> list.get(i) <= list.get(i + 1))
            || IntStream.range(0, list.size() - 1)
            .allMatch(i -> list.get(