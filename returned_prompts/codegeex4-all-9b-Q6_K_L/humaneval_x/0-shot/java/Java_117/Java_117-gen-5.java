import java.util.*;
import java.lang.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        // split the string into words
        String[] words = s.split(" ");
        // create a list to store the result
        List<String> result = new ArrayList<>();
        // iterate over the words
        for (String word : words) {
            // count the number of consonants in the word
            int consonants = 0;
            for (char c : word.toCharArray()) {
                if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != 'A' && c != 'E' && c != 'I' && c != 'O' && c != 'U') {
                    consonants++;
                }
            }
            // if the number of consonants is equal to n, add the word to the result list
            if (consonants == n) {
                result.add(word);
            }
        }
        // return the result list
        return result;
    }
}