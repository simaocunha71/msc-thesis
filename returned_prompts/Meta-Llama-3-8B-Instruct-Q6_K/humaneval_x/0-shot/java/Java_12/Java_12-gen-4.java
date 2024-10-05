    import java.util.*;
    import java.lang.*;

class Solution {
    public Optional<String> longest(List<String> strings) {
        if (strings.isEmpty()) {
            return Optional.empty();
        }
        String longest = strings.get(0);
        for (String str : strings) {
            if (str.length() > longest.length()) {
                longest = str;
            }
        }
        return Optional.of(longest);
    }
}
In this solution, we first check if the input list is empty. If it is, we return an empty Optional. If not, we initialize the longest string to the first string in the list, and then iterate over the list. If we find a string that is longer than the current longest string, we update the longest string. Finally, we return an Optional containing the longest string. If there are multiple strings of the same length, this solution will return the first one. If the input list is empty, it will return an empty Optional.