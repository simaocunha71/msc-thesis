Here's the Java code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<Integer> filteredArr = new ArrayList<>();
        for (Integer i : arr) {
            if (i > 0 && i < 10) {
                filteredArr.add(i);
            }
        }
        Collections.sort(filteredArr);
        Collections.reverse(filteredArr);
        List<String> result = new ArrayList<>();
        for (Integer i : filteredArr) {
            result.add(convert(i));
        }
        return result;
    }

    private String convert(int i) {
        switch (i) {
            case 1: return "One";
            case 2: return "Two";
            case 3: return "Three";
            case 4: return "Four";
            case 5: return "Five";
            case 6: return "Six";
            case 7: return "Seven";
            case 8: return "Eight";
            case 9: return "Nine";
            default: return "";
        }
    }
}
```

In this code, we first filter out the numbers in the range of 1 to 9 and store them in `filteredArr`. Then we sort and reverse this list. Finally, we convert each number into its corresponding string using the `convert` function and store them in `result`. The `convert` function uses a switch statement to return the correct string for each number. If the number is not in the range of 1 to 9, it returns an empty string.