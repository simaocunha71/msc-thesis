import java.util.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        List<String> list = new ArrayList<String>();
        if (s.length() == 0) {
            return list;
        }
        int start = 0;
        int end = 0;
        int count = 0;
        while (end < s.length()) {
            if (Character.isLetter(s.charAt(end))) {
                if (!Character.isWhitespace(s.charAt(end))) {
                    count++;
                    if (count == n) {
                        list.add(s.substring(start, end + 1));
                        start = end + 1;
                        count = 0;
                    }
                }
            }
            end++;
        }
        return list;
    }
}