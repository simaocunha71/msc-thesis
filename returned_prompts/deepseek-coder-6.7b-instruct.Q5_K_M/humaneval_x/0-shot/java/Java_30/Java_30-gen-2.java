        return l.stream().filter(i -> i > 0).collect(Collectors.toList());
    }
}

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.getPositive(Arrays.asList(-1, 2, -4, 5, 6)));
        System.out.println(s.getPositive(Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10)));
    }
}

The program uses Java 8's Stream API to filter out non-positive numbers from the list. The `filter` method filters out elements that do not meet a certain condition. In this case, the condition is `i > 0`, so only positive numbers are kept.

The `collect` method then collects these positive numbers into a new `List`. The `Collectors.toList()` method is used to create a `List`.

The main method creates a new instance of `Solution` and calls the `getPositive` method with a list of integers. The result is then printed to the console.

The expected output is:
[2, 5, 6]
[5, 3, 2, 3, 9, 123, 1]
*/

// -------
// NOTE:
// This is a sample of a potential solution.
// There can be multiple correct solutions.
// -------

import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> getPositive(List<Integer> l) {
        return l.stream().filter(i -> i > 0).collect(Collectors.toList());
    }
}

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.getPositive(Arrays.asList(-1, 2, -4, 5, 6)));
        System.out.println(