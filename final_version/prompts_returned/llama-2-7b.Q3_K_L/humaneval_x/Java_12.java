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
        Map<Integer, String> map = new HashMap<>();
        for (int i = 0; i < strings.size(); i++)
            map.putIfAbsent(i + 1, strings.get(i)) == null ? strings.get(i) : "a" + i; // +1 to get the right index from the map
        return Optional.ofNullable(map.entrySet().iterator().next().getValue());
    }
}
