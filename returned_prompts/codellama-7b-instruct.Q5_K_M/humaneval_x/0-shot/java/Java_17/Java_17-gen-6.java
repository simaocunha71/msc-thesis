import java.util.*;
import java.lang.*;

class Solution {
    /**
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    "o" - whole note, lasts four beats
    "o|" - half note, lasts two beats
    ".|" - quater note, lasts one beat

    >>> parseMusic("o o| .| o| o| .| .| .| .| o o")
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
     */
    public List<Integer> parseMusic(String string) {

        List<Integer> result = new ArrayList<>();
        for (String s : string.split(" ")) {
            if (s.equals("o")) {
                result.add(4);
            } else if (s.equals("o|")) {
                result.add(2);
            } else if (s.equals(".|")) {
                result.add(1);
            } else {
                result.add(0);
            }
        }
        return result;
    }
}

