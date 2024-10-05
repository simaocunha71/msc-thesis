Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<String> wordStrings(String s) {
        List<String> words = new ArrayList<>();
        String[] strArray = s.split("[,\\s]+");
        for (String str : strArray) {
            words.add(str);
        }
        return words;
    }
}
```

In this solution, we use the `split()` method of the `String` class to split the input string `s` into an array of strings. The regular expression `[ ,]+` matches one or more spaces or commas, so the `split()` method splits the input string at each space or comma. We then add each element of the array to a `List<String>` called `words`, and return this list.

For example, if the input string is `"Hi, my name is John"`, the `split()` method will split it into the array `{"Hi", "my", "name", "is", "John"}`, and the `List<String>` `words` will be `{"Hi", "my", "name", "is", "John"}`. If the input string is `"One, two, three, four, five, six"`, the `split()` method will split it into the array `{"One", "two", "three", "four", "five", "six"}`, and the `List<String>` `words` will be `{"One", "two", "three", "four", "five", "six"}`.