        String[] words = s.split(" ");
        StringBuilder res = new StringBuilder();

        for (String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            res.append(new String(chars)).append(" ");
        }

        return res.toString().trim();
    }
}

The function antiShuffle splits the string into words and sorts each word's characters. It then appends each sorted word and a space to a StringBuilder. Finally, it removes any trailing spaces and converts the StringBuilder back to a string.
*/

/**
 * Class for testing the solution.
 */
public class Main {

    /**
     * The main function from where execution starts.
     * @param args Unused.
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.antiShuffle("Hi"));
        System.out.println(solution.antiShuffle("hello"));
        System.out.println(solution.antiShuffle("Hello World!!!"));
    }
}

This program will print:
Hi
ehllo
Hello  !!!Wdlor
*/

//src/main/java/com/example/test/Solution2.java
package com.example.test;

import java.util.Arrays;

public class Solution2 {
    public String antiShuffle(String s) {
        String[] words = s.split(" ");
        StringBuilder res = new StringBuilder();

        for (String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            res.append(new String(chars)).append(" ");
        }

        return res.toString().trim();
    }
}

//src/test/java/com/example/test/SolutionTest.java
package com.example.test;

import com.example.test.Solution;
import org.junit.Test;
import static org.junit.Assert.*;

public class SolutionTest {
    @Test
    public void test