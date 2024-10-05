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
        if (strings.isEmpty()) {
            return "";
        }
        String result = strings.get(0);
        for (int i = 1; i < strings.size(); i++) {
            result += strings.get(i);
        }
        return result;
    }
}
