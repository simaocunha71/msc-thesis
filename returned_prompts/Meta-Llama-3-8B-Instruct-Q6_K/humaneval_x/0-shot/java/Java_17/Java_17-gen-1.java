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

Explanation: 
This problem is asking to parse a string of musical notes and return a list of integers representing the duration of each note. The notes are represented using a special ASCII format, where "o" represents a whole note (4 beats), "o|" represents a half note (2 beats), and ".|" represents a quarter note (1 beat).

The solution uses a simple loop to iterate over the string, splitting it into individual notes using the space character as a delimiter. For each note, it checks the type of note and adds the corresponding duration to the result list.

The time complexity of this solution is O(n), where n is the length of the input string, because it iterates over the string once. The space complexity is O(n) as well, because it creates a list to store the results. 