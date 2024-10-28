```java
import java.util.*;

class Solution {
    public List<Integer> parseMusic(String string) {
        List<Integer> beats = new ArrayList<>();
        String[] notes = string.split(" ");
        for (String note : notes) {
            if (note.equals("o")) {
                beats.add(4);
            } else if (note.equals("o|")) {
                beats.add(2);
            } else if (note.equals(".|")) {
                beats.add(1);
            }
        }
        return beats;
    }
}
```

Explanation:
This solution uses a list to store the beats and then iterates over each note in the input string. If the note is "o", it adds 4 beats to the list. If the note is "o|", it adds 2 beats to the list. If the note is ".|", it adds 1 beat to the list. Finally, it returns the list of beats. The split() function is used to split the input string into an array of notes, and the equals() method is used to check the equality of each note with the given strings. The List<Integer> is used to store the beats. This solution assumes that the input string is well-formed and contains only the specified notes. If the input string can contain other characters, you may need to add error handling code to handle those cases.