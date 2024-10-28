```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<Integer> between1and9 = new ArrayList<>();
        for (int i : arr) {
            if (i >= 1 && i <= 9) {
                between1and9.add(i);
            }
        }
        Collections.sort(between1and9);
        Collections.reverse(between1and9);
        String[] names = {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
        List<String> result = new ArrayList<>();
        for (int i : between1and9) {
            result.add(names[i - 1]);
        }
        return result;
    }
}
```