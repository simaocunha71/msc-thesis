    import java.util.*;

    public class Solution {
        public List<Integer> sortEven(List<Integer> l) {
            List<Integer> result = new ArrayList<>();
            for (int i = 0; i < l.size(); i++) {
                if (i % 2 == 0) {
                    result.add(i, Collections.min(Arrays.asList(l.get(i), l.get(i + 1))));
                } else {
                    result.add(l.get(i));
                }
            }
            return result;
        }
    }
}