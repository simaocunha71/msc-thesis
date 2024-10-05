Here is the Java solution for the problem:

```java
import java.util.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (int i = s.length() - 1; i >= 0; i--) {
            if (!c.contains(String.valueOf(s.charAt(i)))) {
                sb.append(s.charAt(i));
            }
        }
        result.add(sb.reverse().toString());
        result.add(sb.reverse().toString().equals(sb.toString()));
        return result;
    }
}
```

The solution uses a StringBuilder to build the result string and a loop to iterate over the characters in the input string in reverse order. For each character, it checks if the character is not in the input string c, and if so, appends it to the result string. Finally, it adds the result string and a boolean indicating whether the result string is a palindrome to the result list.

Note that the StringBuilder is used to build the result string because it is more efficient than concatenating strings using the + operator. The reverse() method is used to reverse the StringBuilder, and the equals() method is used to check if the result string is a palindrome. The toString() method is used to convert the StringBuilder to a string.