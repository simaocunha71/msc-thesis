        return l.stream()
                .filter(x -> x > 0)
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.getPositive(Arrays.asList(-1, 2, -4, 5, 6))); //[2, 5, 6]
        System.out.println(s.getPositive(Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10))); //[5, 3, 2, 3, 9, 123, 1]
    }
}

*/

import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    /**
    Return only positive numbers in the list.
    >>> getPositive(Arrays.asList(-1, 2, -4, 5, 6))
    [2, 5, 6]
    >>> getPositive(Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10))
    [5, 3, 2, 3, 9, 123, 1]
    */
    public List<Integer> getPositive(List<Integer> l) {
        return l.stream()
                .filter(x -> x > 0)
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.getPositive(Arrays.asList(-1, 2, -4, 5, 6))); //[2, 5, 6]
        System.out.println(s.getPositive(Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1,