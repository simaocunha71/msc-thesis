Here is the solution:
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
The solution iterates over the string `s` and checks each character to see if it is present in the string `c`. If it is not present, it adds the character to a `StringBuilder` object. After iterating over all characters, it converts the `StringBuilder` object to a string and adds it to the result list. It then checks if the resulting string is equal to its reverse and adds the result to the list as well. The list is then returned as the result.

For example, if `s = "abcde"` and `c = "ae"`, the solution will iterate over the characters of `s` and find that 'a' and 'e' are present in `c`. It will then add 'b', 'c', and 'd' to the `StringBuilder` object, resulting in the string "bcd". The solution will then add "bcd" to the result list and check if it is equal to its reverse. Since "bcd" is not equal to its reverse, the solution will add `false` to the list. The final result will be `["bcd", false]`.  If `s = "abcdedcba"` and `c = "ab"`, the solution will iterate over the characters of `s` and find that 'a' and 'b' are present in `c`. It will then add 'c', 'd', 'e', 'd', 'c' to the `StringBuilder` object, resulting in the string "cdeDC". The solution will then add "cdeDC" to the result list and check if it is equal to its reverse. Since "cdeDC" is equal to its reverse, the solution will add `true` to the list. The final result will be `["cdeDC", true]`.  If `s = "abcdef"` and `c = "b"`, the solution will iterate over the characters of `s` and find that 'b' is present