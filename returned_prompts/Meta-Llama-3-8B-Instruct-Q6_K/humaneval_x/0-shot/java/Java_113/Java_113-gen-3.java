Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<String> oddCount(List<String> lst) {
        List<String> result = new ArrayList<>();
        for (String s : lst) {
            int count = 0;
            for (char c : s.toCharArray()) {
                if ((c - '0') % 2 != 0) {
                    count++;
                }
            }
            result.add("the number of odd elements " + count + "n the str" + (s.length() + 1) + "ng " + (s.length() + 1) + " of the " + (s.length() + 1) + "nput.");
        }
        return result;
    }
}
```

The function `oddCount` iterates over each string in the input list, counts the number of odd digits in each string, and then constructs the output string as per the problem statement. The output string contains the count of odd digits, the length of the string (for "str" and "nput" parts), and the length of the string for the "of" part. The result is a list of these output strings. The function returns this list.