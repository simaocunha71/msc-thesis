    return l.stream().filter(x -> x > 0).collect(Collectors.toList());



C:
    import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> getPositive(List<Integer> l) {
        List<Integer> result = new ArrayList<>();
        for (int i : l) {
            if (i > 0) {
                result.add(i);
            }
        }
        return result;
    }
}