Here is a simple Java solution:

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
The `parseMusic` method takes a string as input, splits it into an array of notes using the space character as a delimiter, and then iterates over each note. For each note, it checks the value and adds the corresponding number of beats to the result list. If an invalid note is encountered, an `IllegalArgumentException` is thrown.