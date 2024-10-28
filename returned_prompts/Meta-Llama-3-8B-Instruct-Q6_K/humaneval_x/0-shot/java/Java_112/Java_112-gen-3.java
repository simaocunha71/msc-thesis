Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        StringBuilder sb = new StringBuilder();
        for(int i = s.length() - 1; i >= 0; i--) {
            char ch = s.charAt(i);
            if(!c.contains(String.valueOf(ch))) {
                sb.append(ch);
            }
        }
        String result = sb.reverse().toString();
        return new ArrayList<Object>() {{add(result); add(result.equals(new StringBuilder(result).reverse().toString()));}};
    }
}
```

This program iterates over the input string `s` from right to left (using a StringBuilder to build the result string in reverse order) and checks if each character is present in the string `c`. If the character is not present in `c`, it is added to the result string. After building the result string, it checks if the result string is equal to its reverse (to check if it is a palindrome). The result and the palindrome check are returned as a list of two objects.