    import java.util.*;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "Hi, my name is John";
        List<String> result = solution.wordStrings(s);
        System.out.println(result);
    }
}

class Solution {
    public List<String> wordStrings(String s) {
        List<String> result = new ArrayList<>();
        String[] words = s.split("[\\s,]+");
        for (String word : words) {
            result.add(word);
        }
        return result;
    }
}  



Output:

[Hi, my, name, is, John]

Explanation:
The program defines a class called Solution that has a method wordStrings which takes a string as an input. The method splits the input string into words using the split method and adds each word to a list. The split method uses a regular expression "[\\s,]+" which matches one or more occurrences of whitespace characters or commas. The method then returns the list of words. In the main method, an instance of the Solution class is created and the wordStrings method is called with a string as an argument. The result is printed to the console.  



Time complexity: O(n)
where n is the number of characters in the input string. This is because the split method iterates over the input string once, and the add method of the list also iterates over the input string once. 

Space complexity: O(n)
where n is the number of words in the input string. This is because the list stores all the words in the input string.  



Note: The regular expression "[\\s,]+" matches one or more occurrences of whitespace characters or commas. This is used to split the input string into words. The split method splits the input string into words based on this regular expression.  



Also, the split method returns an array of words, and then each word is added to the list. This is because the split method does not return a list, it returns an array. The add method of the list is used to add each word to the list.  



The program can be modified to handle edge cases such as an empty string or a string with no words. For example, the wordStrings method can return an empty list for an empty string, or can handle a string with no words by returning a list with a single empty string.  



The program can also be modified to handle different types of delimiters, such as semicolons or dashes