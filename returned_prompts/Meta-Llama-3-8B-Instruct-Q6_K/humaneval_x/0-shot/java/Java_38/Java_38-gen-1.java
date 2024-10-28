Here is a solution in Java:

```java
import java.util.*;

class Solution {
    public String encodeCyclic(String s) {
        List<String> groups = new ArrayList<>();
        for (int i = 0; i < s.length(); i += 3) {
            groups.add(s.substring(i, Math.min(i + 3, s.length())));
        }
        for (int i = 0; i < groups.size(); i++) {
            if (groups.get(i).length() == 3) {
                char[] chars = groups.get(i).toCharArray();
                char temp = chars[0];
                chars[0] = chars[2];
                chars[2] = temp;
                groups.set(i, new String(chars));
            }
        }
        return String.join("", groups);
    }

    public String decodeCyclic(String s) {
        List<String> groups = new ArrayList<>();
        for (int i = 0; i < s.length(); i += 3) {
            groups.add(s.substring(i, Math.min(i + 3, s.length())));
        }
        for (int i = 0; i < groups.size(); i++) {
            if (groups.get(i).length() == 2) {
                char[] chars = groups.get(i).toCharArray();
                chars[1] = (char) (chars[1] - 1);
                groups.set(i, new String(chars));
            }
        }
        return String.join("", groups);
    }
}
```

Explanation:

1. The `encodeCyclic` function takes a string as input and returns the encoded string by cycling groups of three characters. It splits the input string into groups of three characters, then cycles the characters in each group unless the group has fewer elements than three.
2. The `decodeCyclic` function takes a string as input and returns the decoded string. It splits the input string into groups of three characters, then decodes each group by incrementing the second character unless the group has fewer elements than three.

Note: The `decodeCyclic` function assumes that the input string is encoded using the same logic as the `encodeCyclic` function. If the input string is encoded differently, the `decodeCyclic` function may not work correctly.