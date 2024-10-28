import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return list of all prefixes from shortest to longest of the input string
    >>> allPrefixes("abc")
    ["a", "ab", "abc"]
     */
    public List<String> allPrefixes(String string) {
        List<String> prefixes = new ArrayList<>();
        int length = string.length();

        for (int i = 0; i < length; i++) {
            String prefix = string.substring(0, i + 1);
            prefixes.add(prefix);
        }

        return prefixes;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.allPrefixes("abc"));
    }
}
