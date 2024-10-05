import java.util.*;
import java.lang.*;

class Solution {
    public String flipCase(String string) {
        String result = "";
        for (char c : string.toCharArray()) {
            if (Character.isUpperCase(c)) {
                result += Character.toLowerCase(c);
            } else {
                result += Character.toUpperCase(c);
            }
        }
        return result;
    }
}
