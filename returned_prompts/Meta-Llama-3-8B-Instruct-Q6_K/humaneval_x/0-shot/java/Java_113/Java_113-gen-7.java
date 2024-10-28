Here is the solution to the problem:

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
            result.add("the number of odd elements " + count + "n the str" + s.length() + "ng " + s.length() + " of the " + s.length() + "nput.");
        }
        return result;
    }
}
```

This solution iterates over each string in the input list, counts the number of odd digits in the string, and then constructs the output string according to the problem description. The `toCharArray()` method is used to iterate over each character in the string, and the `char - '0'` expression is used to convert the character to an integer. The `%` operator is used to check if the digit is odd. The output string is constructed by concatenating the required parts using the `+` operator. Finally, the result list is returned.