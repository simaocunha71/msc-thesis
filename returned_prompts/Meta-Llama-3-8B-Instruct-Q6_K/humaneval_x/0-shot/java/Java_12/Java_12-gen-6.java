import java.util.*;

class Solution {
    public Optional<String> longest(List<String> strings) {
        if (strings.isEmpty()) {
            return Optional.empty();
        }

        Optional<String> longest = Optional.of(strings.get(0));
        for (String s : strings) {
            if (s.length() > longest.get().length()) {
                longest = Optional.of(s);
            } else if (s.length() == longest.get().length()) {
                longest = Optional.of(s);
                break;
            }
        }
        return longest;
    }
}