        String maxWord = "";
        int maxUnique = 0;

        for (String word : words) {
            Set<Character> uniqueChars = new HashSet<>();
            for (char ch : word.toCharArray()) {
                uniqueChars.add(ch);
            }
            if (uniqueChars.size() > maxUnique ||
                (uniqueChars.size() == maxUnique && word.compareTo(maxWord) < 0)) {
                maxUnique = uniqueChars.size();
                maxWord = word;
            }
        }

        return maxWord;
    }
}

*/

//src/main/java/com/example/codewars/maxUniqueChars/MaxUniqueCharsTest.java
package com.example.codewars.maxUniqueChars;

import com.example.codewars.maxUniqueChars.Solution;
import org.junit.Test;
import static org.junit.Assert.*;

public class MaxUniqueCharsTest {

    @Test
    public void testFindMax() {
        Solution solution = new Solution();
        assertEquals("string", solution.findMax(java.util.Arrays.asList("name", "of", "string")));
        assertEquals("enam", solution.findMax(java.util.Arrays.asList("name", "enam", "game")));
        assertEquals("aaaaaaa", solution.findMax(java.util.Arrays.asList("aaaaaaa", "bb", "cc")));
        assertEquals("", solution.findMax(java.util.Arrays.asList("aaaaaaa", "", "cc")));
    }
}

//src/main/java/com/example/codewars/palindrome/Palindrome.java
package com.example.codewars.palindrome;

public class Palindrome {
    public static boolean isPalindrome(String str) {
        String cleanStr = str.replaceAll("\\W", "");
        StringBuilder s = new StringBuilder(cleanStr);
        String reverse = s.reverse().toString();
        return reverse.equals(cleanStr);
