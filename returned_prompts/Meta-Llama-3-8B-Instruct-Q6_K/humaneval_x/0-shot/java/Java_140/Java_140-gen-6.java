public class Solution {
    public String fixSpaces(String text) {
        StringBuilder result = new StringBuilder();
        int count = 0;
        for (char c : text.toCharArray()) {
            if (c == ' ') {
                count++;
                if (count > 2) {
                    result.append('-');
                    count = 0;
                } else {
                    if (count == 1) {
                        result.append('_');
                    }
                    result.append(' ');
                    count = 0;
                }
            } else {
                result.append(c);
                count = 0;
            }
        }
        return result.toString();
    }
}
