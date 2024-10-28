public class Solution {
    public static String concatenate(List<String> strings) {
        if (strings.isEmpty()) {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        for (String s : strings) {
            sb.append(s);
        }
        return sb.toString();
    }
}
