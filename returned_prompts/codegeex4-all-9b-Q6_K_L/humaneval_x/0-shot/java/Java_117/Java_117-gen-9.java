import java.util.*;
import java.lang.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        List<String> list = new ArrayList<String>();
        String[] words = s.split(" ");
        for (String word : words) {
            int consonants = 0;
            for (char c : word.toCharArray()) {
                if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != 'A' && c != 'E' && c != 'I' && c != 'O' && c != 'U') {
                    consonants++;
                }
            }
            if (consonants == n) {
                list.add(word);
            }
        }
        return list;
    }
}