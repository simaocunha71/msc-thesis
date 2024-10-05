import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> getPositive(List<Integer> l) {
        return l.stream()
            .filter(n -> n > 0)
            .collect(Collectors.toList());
    }
}