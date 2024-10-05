        String result = text.replace("  ", "-");
        result = result.replace(" ", "_");

        if (result.length() > 0 && result.charAt(0) == '-') {
            result = result.substring(1);
        }

        if (result.length() > 0 && result.charAt(result.length() - 1) == '-') {
            result = result.substring(0, result.length() - 1);
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.fixSpaces("Example"));
        System.out.println(solution.fixSpaces("Example 1"));
        System.out.println(solution.fixSpaces(" Example 2"));
        System.out.println(solution.fixSpaces(" Example  3"));
    }
}


A: You can use the built-in String.replaceAll() method with a regular expression.
The regular expression "\\s{2,}" matches any occurrence of 2 or more consecutive spaces. The "\\s" matches any space character. The "{2,}" is a quantifier that means "match 2 or more of the preceding".
You can replace these sequences with underscores, and sequences of just one space with an underscore.
Then, if the resulting string starts or ends with a hyphen, you can remove it.
Here's the code:
public String fixSpaces(String text) {
    String result = text.replaceAll("\\s{2,}", "-").replace(" ", "_");
    if (result.startsWith("-")) {
        result = result.substring(1);
    }
    if (result.endsWith("-")) {
        result = result.substring(0, result.length() - 1);
    }
    return result;
}


A: Here is the solution:

import java.util.*;
import java.lang.*;

class Solution {
    public String fixSpaces(String text) {
        StringBuilder result = new StringBuilder();
        boolean isPrevSpace = false;
