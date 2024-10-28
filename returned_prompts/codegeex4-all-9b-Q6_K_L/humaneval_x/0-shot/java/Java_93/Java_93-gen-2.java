import java.util.*;
import java.lang.*;

class Solution {
    public String encode(String message) {
        StringBuilder sb = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isUpperCase(c)) {
                char lower = Character.toLowerCase(c);
                if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u') {
                    sb.append((char) (lower + 2));
                } else {
                    sb.append(lower);
                }
            } else {
                char upper = Character.toUpperCase(c);
                if (upper == 'A' || upper == 'E' || upper == 'I' || upper == 'O' || upper == 'U') {
                    sb.append((char) (upper + 2));
                } else {
                    sb.append(upper);
                }
            }
        }
        return sb.toString();
    }
}