    import java.util.*;

    public class Solution {
        public List<String> filterBySubstring(List<String> strings, String substring) {
            List<String> result = new ArrayList<>();
            for (String s : strings) {
                if (s.contains(substring)) {
                    result.add(s);
                }
            }
            return result;
        }
    } 














