import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> removeDuplicates(List<Integer> numbers) {
        List<Integer> result = new ArrayList<>();
        Set<Integer> seen = new HashSet<>();
        for (Integer number : numbers) {
            if (!seen.contains(number)) {
                seen.add(number);
                result.add(number);
            }
        }
        return result;
    }
}