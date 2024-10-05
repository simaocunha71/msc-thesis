import java.util.*;
import java.lang.*;

class Solution {
    public int solution(List<Integer> lst) {
        return lst.stream()
                .filter((t, i) -> i % 2 == 0 && t % 2 != 0)
                .mapToInt(Integer::intValue)
                .sum();
    }
}