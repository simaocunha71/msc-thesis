```java
import java.util.*;

public class Solution {
    public List<String> wordStrings(String s) {
        // Split the string into words
        String[] words = s.split("[,\\s]+");

        // Convert the array to a list
        List<String> result = new ArrayList<>(Arrays.asList(words));

        return result;
    }
}
```

The code above defines a method `wordStrings` that takes a string `s` as input, splits it into words using a regular expression `[,\\s]+` (which matches one or more commas or spaces), and returns a list of the words. The `split` method returns an array of strings, which is then converted to a list using the constructor of the `ArrayList` class. This approach ensures that the original order of the words is preserved.

The regular expression `[,\\s]+` is used to split the string into words. This expression matches one or more occurrences of either a comma (`,`) or a space (`\\s`). The `+` quantifier specifies that the preceding pattern should be matched one or more times.

For example, if the input string is `"Hi, my name is John"`, the `split` method will split it into the following array of words: `["Hi", "my", "name", "is", "John"]`. The list resulting from this operation will be `["Hi", "my", "name", "is", "John"]`, which is the expected output.