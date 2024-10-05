import java.util.*;
import java.lang.*;

class Solution {
    /**
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest(List.of())
    Optional.empty
    >>> longest(Arrays.asList("a", "b", "c"))
    Optional[a]
    >>> longest(Arrays.asList("a", "bb", "ccc"))
    Optional[ccc]
     */
    public Optional<String> longest(List<String> strings) {
        return strings.stream().max(Comparator.comparingInt(String::length));
    }

    /**
    Return the sum of all numbers in the list.
    >>> sum(List.of(1, 2, 3))
    6
    >>> sum(List.of(1, 2, 3, 4, 5))
    15
    >>> sum(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    55
    */
    public int sum(List<Integer> numbers) {
        return numbers.stream().mapToInt(i -> i).sum();
    }

    /**
    Return the list of strings sorted lexicographically.
    >>> sorted(List.of("a", "b", "c"))
    List[a, b, c]
    >>> sorted(List.of("b", "a"))
    List[a, b]
    >>> sorted(List.of("c", "a", "b"))
    List[a, b, c]
     */
    public List<String> sorted(List<String> strings) {
        return strings.stream().sorted().collect(Collectors.toList());
    }
}
