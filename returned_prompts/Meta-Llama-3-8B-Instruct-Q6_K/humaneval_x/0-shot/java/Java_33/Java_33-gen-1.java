import java.util.*;

class Solution {
    public List<Integer> sortThird(List<Integer> l) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                result.add(i, Collections.max(Arrays.stream(l.subList(i, l.size())).boxed().collect(Collectors.toList())));
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
}