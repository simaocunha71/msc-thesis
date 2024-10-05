import java.util.*;
import java.lang.*;

class Solution {
    public Object splitWords(String txt) {
        if (txt.indexOf(' ') >= 0) {
            return txt.split(" ");
        } else if (txt.indexOf(',') >= 0) {
            return txt.split(",");
        } else {
            int count = 0;
            for (char c : txt.toCharArray()) {
                if (Character.isLowerCase(c) && (c - 'a') % 2 == 1) {
                    count++;
                }
            }
            return count;
        }
    }
}