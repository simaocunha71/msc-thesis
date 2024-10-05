import java.util.*;

class Solution {
    public String findMax(List<String> words) {

        // your code goes here
        Map<Character, Integer> map = new HashMap<>();
        String max = "";
        for (String word : words) {
            for (int i = 0; i < word.length(); i++) {
                char ch = word.charAt(i);
                if (map.containsKey(ch)) {
                    map.put(ch, map.get(ch) + 1);
                } else {
                    map.put(ch, 1);
                }
            }
            if (word.length() > max.length() || (word.length() == max.length() && word.compareTo(max) < 0)) {
                max = word;
            }
            map.clear();
        }
        return max;
    }
}
