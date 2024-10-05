import java.util.*;
import java.lang.*;

class Solution {
    public Optional<String> longest(List<String> strings) {
        Optional<String> longest = Optional.empty();
        for (String s : strings) {
            if (longest.isEmpty() || s.length() > longest.get().length()) {
                longest = Optional.of(s);
            }
        }
        return longest;
    }
}