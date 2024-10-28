Here is the Java implementation for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> parseMusic(String string) {
        List<Integer> beats = new ArrayList<>();
        String[] notes = string.split(" ");
        for (String note : notes) {
            switch (note) {
                case "o":
                    beats.add(4);
                    break;
                case "o|":
                    beats.add(2);
                    break;
                case ".|":
                    beats.add(1);
                    break;
                default:
                    beats.add(0);
                    break;
            }
        }
        return beats;
    }
}
```

This implementation splits the input string into an array of notes and then iterates over the array. For each note, it checks its value and adds the corresponding number of beats to the list. If the note is not recognized, it adds 0 beats.