        return l.stream().filter(i -> i > 0).collect(Collectors.toList());

    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.getPositive(Arrays.asList(-1, 2, -4, 5, 6)));
        System.out.println(sol.getPositive(Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10)));
    }
}

The solution uses Java 8 streams to filter the list. The filter function takes a lambda expression that is used to check each element of the stream. If the element is greater than 0 (`i > 0`), it's included in the new list. The result is collected back into a list using the `collect` function.

Note:
Make sure you have Java 8 or later installed because Java 8 introduced the Stream API which allows for functional-style operations on collections.
*/

import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> getPositive(List<Integer> l) {
        return l.stream().filter(i -> i > 0).collect(Collectors.toList());
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.getPositive(Arrays.asList(-1, 2, -4, 5, 6)));
        System.out.println(sol.getPositive(Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10)));
    }
}

//testcases/positive/positive_negative_zero.java
/*
