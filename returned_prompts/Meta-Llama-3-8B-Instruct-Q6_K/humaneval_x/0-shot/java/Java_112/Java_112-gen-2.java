Here is the solution for the problem:

```java
import java.util.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (!c.contains(String.valueOf(ch))) {
                sb.append(ch);
            }
        }
        String res = sb.toString();
        result.add(res);
        result.add(res.equals(new StringBuilder(res).reverse().toString()));
        return result;
    }
}
```

This solution iterates over the input string `s` and for each character, it checks if the character is present in the string `c`. If the character is not present in `c`, it adds the character to a `StringBuilder`. After iterating over the entire string, it converts the `StringBuilder` to a string and adds it to the result list. Then, it checks if the string is palindrome by comparing it with its reverse and adds the result to the list. The list contains the result string and the palindrome check result.

For example, if the input is `s = "abcde"` and `c = "ae"`, the output will be `["bcd", false]`. If the input is `s = "abcdedcba"` and `c = "ab"`, the output will be `["cdedc", true]`.  If the input is `s = "abcdef"` and `c = "b"`, the output will be `["acdef", false]`. 