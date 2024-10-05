        List<String> prefixes = new ArrayList<>();
        for (int i = 0; i < string.length(); i++) {
            prefixes.add(string.substring(0, i + 1));
        }
        return prefixes;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.allPrefixes("abc"));
    }
}

The solution is a simple one: we use a for loop to go through the string from the first character to the last. On each iteration, we add a new substring to the list. This substring starts at the first character and goes up to the current character of the loop (i + 1 because substring indices are zero-based). When the loop finishes, we return the list.
*/

import java.util.*;

class Solution {
    public List<String> allPrefixes(String string) {
        List<String> prefixes = new ArrayList<>();
        for (int i = 0; i < string.length(); i++) {
            prefixes.add(string.substring(0, i + 1));
        }
        return prefixes;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.allPrefixes("abc"));
    }
}

// Output: [a, ab, abc]

/*
This solution is correct and efficient. It iterates through the string only once, so its time complexity is O(n), where n is the length of the string. It stores the prefixes in an ArrayList, so its space complexity is also O(n).
*/

// 