import java.util.*;
import java.lang.*;

class Solution {
    /**
    Concatenate list of strings into a single string
    >>> concatenate(List.of())
    ""
    >>> concatenate(Arrays.asList("a", "b", "c"))
    "abc"
     */
    public String concatenate(List<String> strings) {
        StringBuilder sb = new StringBuilder();
        for (int i=0;i<strings.size();++i){sb.append(strings.get(i));}
        return sb.toString();
        
    }
     */
     /**
    Calculate the sum of all elements in a list
    >>> sum(List.of())
    0L
    >>> sum(Arrays.asList(1,2,3))
    6L
     */
    public long sum(List<Integer> integers) {
        if (integers == null || integers.isEmpty()){return 0L;}
        return integers.stream().mapToLong(n -> n).sum();
        
    }
}
