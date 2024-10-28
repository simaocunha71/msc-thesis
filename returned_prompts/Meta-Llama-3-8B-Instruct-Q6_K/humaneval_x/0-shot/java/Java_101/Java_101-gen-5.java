    import java.util.*;

    class Solution {
        public List<String> wordStrings(String s) {
            String[] words = s.split("[,\\s]+");
            List<String> result = new ArrayList<>();
            for (String word : words) {
                if (!word.isEmpty()) {
                    result.add(word);
                }
            }
            return result;
        }
    }

Explanation:
The given problem is asking to split a string of words separated by commas or spaces into an array of words. The words are considered as any sequence of characters separated by commas or spaces.

In the solution, we use the `split()` method of the `String` class to split the given string `s` into an array of words. The regular expression `[\\s,]+` matches one or more occurrences of either a space character or a comma.

We then create a `List` to store the words. We iterate over the array of words and add each non-empty word to the `List`. This ensures that we only include words that are not empty strings.

Finally, we return the `List` of words. This solution is efficient and easy to understand, making it suitable for the given problem.