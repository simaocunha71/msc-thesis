import java.util.*;

class Solution {
    public static void main(String[] args) {
        List<String> list = Arrays.asList("a", "b", "c");
        System.out.println(longest(list));
    }
    
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
    public static Optional<String> longest(List<String> strings) {
        if (strings.isEmpty()) return Optional.empty();
        Collections.sort(strings, (s1, s2) -> s2.length() - s1.length());
        return Optional.of(strings.get(0));
    }
}
