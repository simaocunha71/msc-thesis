    import java.util.*;

    public class Solution {
        public Optional<String> longest(List<String> strings) {
            if (strings.isEmpty()) {
                return Optional.empty();
            }
            String longestStr = strings.get(0);
            for (String str : strings) {
                if (str.length() > longestStr.length()) {
                    longestStr = str;
                }
            }
            return Optional.of(longestStr);
        }
    }  // The longest method iterates over the list of strings. It starts with the first string as the longest. Then it checks each subsequent string. If it's longer, it becomes the new longest. At the end, it returns the longest string as an Optional. If the list is empty, it returns an empty Optional.