Here is a Java solution using a helper function to count the number of consonants in a word:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        List<String> result = new ArrayList<>();
        String[] words = s.split(" ");
        for (String word : words) {
            if (countConsonants(word) == n) {
                result.add(word);
            }
        }
        return result;
    }

    private int countConsonants(String word) {
        int count = 0;
        for (char c : word.toLowerCase().toCharArray()) {
            if (c >= 'b' && c <= 'z' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.selectWords("Mary had a little lamb", 4)); // ["little"]
        System.out.println(solution.selectWords("Mary had a little lamb", 3)); // ["Mary", "lamb"]
        System.out.println(solution.selectWords("simple white space", 2)); // []
        System.out.println(solution.selectWords("Hello world", 4)); // ["world"]
        System.out.println(solution.selectWords("Uncle sam", 3)); // ["Uncle"]
    }
}
```

This solution works by splitting the input string into words, then for each word it counts the number of consonants by iterating over each character and checking if it is a consonant. If the count of consonants is equal to the input number, the word is added to the result list. The `countConsonants` helper function is used to count the number of consonants in a word.