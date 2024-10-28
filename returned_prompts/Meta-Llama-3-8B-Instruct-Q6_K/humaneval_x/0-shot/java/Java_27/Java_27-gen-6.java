public class Solution {
    public String flipCase(String s) {
        StringBuilder res = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLowerCase(c)) {
                res.append(Character.toUpperCase(c));
            } else {
                res.append(Character.toLowerCase(c));
            }
        }
        return res.toString();
    }
}