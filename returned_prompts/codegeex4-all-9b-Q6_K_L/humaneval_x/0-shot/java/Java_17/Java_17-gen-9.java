Here is a Java solution to your problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> parseMusic(String string) {
        List<Integer> music = new ArrayList<>();
        String[] notes = string.split(" ");
        for (String note : notes) {
            if (note.equals("o")) {
                music.add(4);
            } else if (note.equals("o|")) {
                music.add(2);
            } else if (note.equals(".|")) {
                music.add(1);
            }
        }
        return music;
    }
}
```
This code splits the input string into individual notes using the space character as a delimiter. Then, for each note, it checks the note type and adds the corresponding number of beats to the list. The method then returns the list.