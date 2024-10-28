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
            }
        }
        return result;
    }
}