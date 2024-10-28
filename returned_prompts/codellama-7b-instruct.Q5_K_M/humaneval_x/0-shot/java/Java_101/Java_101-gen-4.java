import java.util.*;
import java.lang.*;

class Solution {
    /**
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John").equals(Arrays.asList("Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six").equals(Arrays.asList("One", "two", "three", "four", "five", "six"]
     */
    public List<String> wordStrings(String s) {
        String[] words = s.split(" ");
        List<String> wordList = new ArrayList<String>();
        
        for (String word: words) {
            wordList.add(word);
        }
        
        return wordList;
    }
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        String[] testCases = {"Hi, my name is John", "One, two, three, four, five, six"};
        String[] expected = {"Hi", "my", "name", "is", "John", "One", "two", "three", "four", "five", "six"};
        
        for (int i = 0; i < testCases.length; i++) {
            List<String> result = sol.wordStrings(testCases[i]);
            if (!result.equals(Arrays.asList(expected[i]))) {
                System.out.println("Test case " + (i+1) + " failed.");
            }
        }
    }
}
