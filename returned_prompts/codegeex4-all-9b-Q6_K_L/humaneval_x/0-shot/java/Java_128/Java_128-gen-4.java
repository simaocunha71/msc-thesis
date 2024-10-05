import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        int sum = 0;
        int sign = 1;
        if (arr.size() == 0) {
            return Optional.empty();
        }
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) < 0) {
                sign = -sign;
            } else if (arr.get(i) == 0) {
                sign = 0;
                break;
            }
            sum += Math.abs(arr.get(i));
        }
        return Optional.of(sum * sign);
    }
}