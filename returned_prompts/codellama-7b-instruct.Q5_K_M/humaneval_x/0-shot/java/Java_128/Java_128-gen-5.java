import java.util.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        if (arr.isEmpty()) {
            return Optional.empty();
        }
        int sum = 0;
        int prod = 1;
        for (int num : arr) {
            sum += Math.abs(num);
            prod *= num > 0 ? 1 : num < 0 ? -1 : 0;
        }
        return Optional.of(sum * prod);
    }
}
