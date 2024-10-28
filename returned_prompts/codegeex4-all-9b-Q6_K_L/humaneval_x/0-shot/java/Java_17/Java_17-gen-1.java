You can solve this problem by iterating over the string and checking for each character.
If the character is "o", you add 4 to the current beat.
If the character is "|", you add the current beat to the result list and reset the current beat to 0.
If the character is ".", you add 1 to the current beat.
Here is the complete code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> parseMusic(String string) {
        List<Integer> result = new ArrayList<>();
        int currentBeat = 0;
        for (char c : string.toCharArray()) {
            switch (c) {
                case 'o':
                    currentBeat += 4;
                    break;
                case '|':
                    result.add(currentBeat);
                    currentBeat = 0;
                    break;
                case '.':
                    currentBeat += 1;
                    break;
            }
        }
        result.add(currentBeat);
        return result;
    }
}
```