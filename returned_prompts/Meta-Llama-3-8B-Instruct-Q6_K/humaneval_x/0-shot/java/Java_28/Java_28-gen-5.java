```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Concatenate list of strings into a single string
    >>> concatenate(List.of())
    ""
    >>> concatenate(Arrays.asList("a", "b", "c"))
    "abc"
     */
    public String concatenate(List<String> strings) {
        StringBuilder sb = new StringBuilder();
        for (String s : strings) {
            sb.append(s);
        }
        return sb.toString();
    }
}
```

Explanation:
In this solution, we use a `StringBuilder` object to concatenate the list of strings into a single string. We iterate over the list of strings using a for-each loop and append each string to the `StringBuilder` object. Finally, we return the string representation of the `StringBuilder` object.

Note that we use a `StringBuilder` object instead of the `+` operator to concatenate the strings. This is because the `+` operator creates a new string object for each concatenation, which can be inefficient for large lists of strings. The `StringBuilder` class, on the other hand, is designed for efficient string concatenation and can handle large amounts of data.