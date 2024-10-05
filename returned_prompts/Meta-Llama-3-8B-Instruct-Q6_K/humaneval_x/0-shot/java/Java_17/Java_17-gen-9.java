Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public List<Integer> parseMusic(String string) {
        List<Integer> result = new ArrayList<>();
        StringBuilder currentNote = new StringBuilder();
        for (char c : string.toCharArray()) {
            if (c == 'o' || c == '.' || c == '|') {
                if (currentNote.length() > 0) {
                    int beats = getBeats(currentNote.toString());
                    result.add(beats);
                    currentNote = new StringBuilder();
                }
                if (c == 'o') {
                    currentNote.append("o");
                } else if (c == '.') {
                    currentNote.append(".");
                } else {
                    currentNote.append("|");
                }
            }
        }
        if (currentNote.length() > 0) {
            int beats = getBeats(currentNote.toString());
            result.add(beats);
        }
        return result;
    }

    private int getBeats(String note) {
        if (note.startsWith("o")) {
            return 4;
        } else if (note.startsWith(".|")) {
            return 2;
        } else if (note.startsWith(".| ")) {
            return 1;
        } else {
            throw new RuntimeException("Invalid note: " + note);
        }
    }
}
```
In this code, we iterate over the input string character by character. If we encounter a character that is not a note, we ignore it. If we encounter a note, we add it to the current note string. When we encounter a note that is different from the previous one (or if it's the first note), we parse the current note and add the corresponding number of beats to the result list. Finally, we add the beats for the last note to the result list. The `getBeats` method is used to parse the note and return the corresponding number of beats. If the note is invalid, it throws a `RuntimeException`. The result is a list of integers representing the number of beats for each note.