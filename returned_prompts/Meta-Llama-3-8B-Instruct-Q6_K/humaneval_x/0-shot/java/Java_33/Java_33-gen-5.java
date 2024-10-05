    import java.util.*;

    public class Solution {
        public List<Integer> sortThird(List<Integer> l) {
            List<Integer> result = new ArrayList<>();
            for (int i = 0; i < l.size(); i++) {
                if (i % 3 == 0) {
                    result.add(i, Collections.max(Arrays.asList(l.get(i), l.get(i + 1), l.get(i + 2))));
                } else {
                    result.add(l.get(i));
                }
            }
            return result;
        }
    }
} 





