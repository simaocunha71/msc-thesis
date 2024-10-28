import java.util.*;

class Solution {
    public int countDistinctCharacters(String string) {
        int count = 0;
        for (char ch : string.toLowerCase().toCharArray()) {
            if (Character.isLetter(ch)) {
                count++;
            }
        }
        return count;
    }
}
