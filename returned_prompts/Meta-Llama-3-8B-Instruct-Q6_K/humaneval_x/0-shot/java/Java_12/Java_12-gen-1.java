Here is the solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<String> longest(List<String> strings) {
        if (strings.isEmpty()) {
            return Optional.empty();
        }
        Optional<String> longest = Optional.empty();
        for (String s : strings) {
            if (longest.isEmpty() || s.length() > longest.get().length()) {
                longest = Optional.of(s);
            }
        }
        return longest;
    }
}
```
This solution iterates over the list of strings. If the list is empty, it returns an empty optional. If the list is not empty, it initializes the longest optional with the first string in the list. Then it iterates over the rest of the strings in the list. If it finds a string that is longer than the current longest, it updates the longest optional with the new longest string. Finally, it returns the longest optional.

Note: The `Optional` class is part of the Java 8 standard library. It is used to represent a container that may or may not contain a non-null value. It is often used to avoid null pointer exceptions in Java. The `get()` method of the `Optional` class returns the value if it is present, and throws a `NoSuchElementException` if it is not present. The `of()` method of the `Optional` class returns an `Optional` containing the given value, or an empty `Optional` if the value is null. The `empty()` method of the `Optional` class returns an empty `Optional`. The `isPresent()` method of the `Optional` class returns true if the value is present, and false otherwise. The `ifPresent()` method of the `Optional` class takes a consumer that is called if the value is present. The `orElse()` method of the `Optional` class returns the value if it is present, and the default value if it is not present. The `orElseGet()` method of the `Optional` class returns the value if it is present, and the default value if it is not present. The `orElseThrow()` method of the `Optional` class returns the value if it is present, and throws an exception if it is not present. The `map()` method of the `Optional` class takes a function that is applied to the value if it is present, and returns an `Optional` containing the result. The `filter()` method of the `Optional` class takes a predicate that is applied to the value