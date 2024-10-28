import java.util.*;
import java.lang.*;

class Solution {
    public Object splitWords(String txt) {
        List<String> words = new ArrayList<>();
        String[] splitByWhitespace = txt.split(" ");
        for (String s : splitByWhitespace) {
            if (s.contains(",")) {
                words.add(s.replace(",", ""));
            } else {
                words.add(s);
            }
        }
        if (words.size() > 0) {
            return words;
        } else {
            int counter = 0;
            for (char c : txt.toCharArray()) {
                if (Character.isLowerCase(c) && c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
                    counter++;
                }
            }
            return counter;
        }
    }
}