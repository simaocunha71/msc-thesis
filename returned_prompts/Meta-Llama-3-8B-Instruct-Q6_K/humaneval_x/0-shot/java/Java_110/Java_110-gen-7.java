Here is a Java solution that uses a simple iteration to solve the problem:

```java
import java.util.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 != 0) {
                boolean found = false;
                for (int j = 0; j < lst2.size(); j++) {
                    if (lst2.get(j) % 2 == 0) {
                        result.add(lst1.get(i));
                        lst2.set(j, lst1.get(i));
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    return "NO";
                }
            } else {
                result.add(lst1.get(i));
            }
        }
        return "YES";
    }
}
```

This solution iterates over the first list and checks if each element is even. If it is not even, it iterates over the second list to find an even number to replace it. If it finds an even number, it adds the original element to the result list and replaces the even number in the second list. If it does not find an even number, it returns "NO". If it can replace all odd numbers, it returns "YES". The result list contains the modified first list with only even numbers.