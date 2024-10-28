        List<String> result = new ArrayList<>();
        String[] words = s.split(" ");
        for (String word : words) {
            int count = 0;
            for (char c : word.toCharArray()) {
                if (Character.toString(c).matches("[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]")) {
                    count++;
                }
            }
            if (count == n) {
                result.add(word);
            }
        }
        return result;
    }
}


A: You can solve this problem by using a simple approach.
First, you should write a method to check if a character is a consonant. 
Then, iterate over each word in the string. For each word, count the number of consonants. If the count matches the target number of consonants, add the word to your result list. 
Finally, return the result list. 

Here's the code:
import java.util.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        List<String> result = new ArrayList<>();
        String[] words = s.split(" ");
        for (String word : words) {
            int count = 0;
            for (char c : word.toCharArray()) {
                if (isConsonant(c)) {
                    count++;
                }
            }
            if (count == n) {
                result.add(word);
            }
        }
        return result;
    }

    private boolean isConsonant(char c) {
        String consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
        return consonants.indexOf(c) >= 0;
    }
}

This code works by splitting the input string into words, then checking each word to see if it contains the exact number of consonants you're looking for. If it does, it adds it to the result list.

A: You can use the following regular expression to count