Here is a possible solution in Java:

```java
import java.util.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        int oddCount = 0;
        for (int num : lst1) {
            if (num % 2 != 0) {
                oddCount++;
            }
        }
        for (int num : lst2) {
            if (num % 2 == 0) {
                oddCount--;
            }
        }
        return oddCount <= 0 ? "YES" : "NO";
    }
}
```

Explanation:

1. The function `exchange` takes two lists of numbers as input, `lst1` and `lst2`.

2. We initialize a variable `oddCount` to keep track of the number of odd numbers in `lst1`.

3. We iterate through `lst1` and check if each number is odd. If it is, we increment `oddCount`.

4. We iterate through `lst2` and check if each number is even. If it is, we decrement `oddCount`.

5. After the loops, if `oddCount` is less than or equal to 0, it means we can exchange enough even numbers from `lst2` to make all the numbers in `lst1` even. In this case, we return "YES".

6. Otherwise, we return "NO".