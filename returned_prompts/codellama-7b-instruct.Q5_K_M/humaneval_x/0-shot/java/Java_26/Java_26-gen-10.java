import java.util.*;

class Solution {
    public List<Integer> removeDuplicates(List<Integer> numbers) {
        return numbers.stream().distinct().collect(Collectors.toList());
    }
}
