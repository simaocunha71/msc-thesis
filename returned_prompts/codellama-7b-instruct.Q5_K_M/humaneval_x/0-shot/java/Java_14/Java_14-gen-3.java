import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return list of all prefixes from shortest to longest of the input string
    >>> allPrefixes("abc")
    ["a", "ab", "abc"]
     */
    public List<String> allPrefixes(String string) {
        List<String> list = new ArrayList<String>();
        for (int i = 0; i < string.length(); i++) {
            list.add(string.substring(0, i + 1));
        }
        return list;
    }
}
