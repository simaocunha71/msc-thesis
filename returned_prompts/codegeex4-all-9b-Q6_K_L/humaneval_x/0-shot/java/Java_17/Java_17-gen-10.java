Here is the Java code to solve the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> parseMusic(String string) {
        List<Integer> result = new ArrayList<>();
        String[] notes = string.split(" ");
        for (String note : notes) {
            switch (note) {
                case "o":
                    result.add(4);
                    break;
                case "o|":
                    result.add(2);
                    break;
                case ".|":
                    result.add(1);
                    break;
                default:
                    throw new IllegalArgumentException("Invalid note: " + note);
            }
        }
        return result;
    }
}
```

Explanation:
- The function `parseMusic` takes a string as input and splits it into an array of individual notes using the `split` method.
- It then iterates over each note and checks its value using a `switch` statement.
- If the note is "o", it adds 4 to the result list.
- If the note is "o|", it adds 2 to the result list.
- If the note is ".|", it adds 1 to the result list.
- If the note is any other value, it throws an `IllegalArgumentException` with a message indicating that the note is invalid.
- Finally, it returns the result list.