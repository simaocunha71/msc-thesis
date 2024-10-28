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
        if(strings.size() == 0) return Optional.empty();
        Optional<String> res = Optional.of(strings.get(0));
        for(String s : strings){
            if(s.length() > res.get().length()){
                res = Optional.of(s);
            }
        }
        return res;
    }
}
