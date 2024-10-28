    import java.util.*;

    public class Solution {
        public int countDistinctCharacters(String s) {
            s = s.toLowerCase();
            Set<Character> set = new HashSet<>();
            for (char c : s.toCharArray()) {
                set.add(c);
            }
            return set.size();
        }
    }
}