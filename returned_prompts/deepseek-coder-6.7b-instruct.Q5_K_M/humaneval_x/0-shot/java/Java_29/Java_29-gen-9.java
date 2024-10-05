        return strings.stream()
                .filter(s -> s.startsWith(prefix))
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.filterByPrefix(Arrays.asList("abc", "bcd", "cde", "array"), "a"));
    }
}

Explanation:
The solution uses Java Stream API to filter the input list. The filterByPrefix method returns a List that includes only the Strings from the input list that start with the given prefix. The filter condition `s.startsWith(prefix)` checks for this.

The main method tests the solution with a list of strings and a prefix "a". It should output ["abc", "array"].
*/

import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {

    public List<String> filterByPrefix(List<String> strings, String prefix) {
        return strings.stream()
                .filter(s -> s.startsWith(prefix))
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.filterByPrefix(Arrays.asList("abc", "bcd", "cde", "array"), "a"));
    }
}

/*
Output:
[abc, array]
*/

//Explanation:
//The solution uses Java Stream API to filter the input list. The filterByPrefix method returns a List that includes only the Strings from the input list that start with the given prefix. The filter condition `s.startsWith(prefix)` checks for this.
//
//The main method tests the solution with a list of strings and a prefix "a". It should output ["abc", "array"].
//
//In the main method, we create an instance of Solution class and call the filterByPrefix method. The method filterByPrefix takes two arguments: a list of strings and a prefix. It returns a new list which includes only the strings from the original list that