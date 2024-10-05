Here is a Java solution:

```java
import java.util.*;

class Solution {
    public List<Integer> parseMusic(String string) {
        List<Integer> result = new ArrayList<>();
        String[] notes = string.split(" ");
        for (String note : notes) {
            if (note.equals("o")) {
                result.add(4);
            } else if (note.equals("o|")) {
                result.add(2);
            } else if (note.equals(".|")) {
                result.add(1);
            }
        }
        return result;
    }
}
```

This solution splits the input string into individual notes, and then checks each note to determine its duration. The duration is then added to the result list. The result list is then returned.

The `split` method is used to split the input string into individual notes. This method splits a string into an array of strings, using a specified delimiter. In this case, the delimiter is a space character.

The `for` loop is used to iterate over each note in the array of notes. The `if` statement is used to check each note to determine its duration. If the note is an "o", its duration is 4. If the note is an "o|", its duration is 2. If the note is a ".|", its duration is 1. The duration is then added to the result list.

Finally, the result list is returned. This list contains the durations of each note in the input string. For example, if the input string is "o o| .| o| o| .| .| .| .| o o", the result list will be `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`. This is because the first note is a whole note (4 beats), the second note is a half note (2 beats), the third note is a quarter note (1 beat), and so on.