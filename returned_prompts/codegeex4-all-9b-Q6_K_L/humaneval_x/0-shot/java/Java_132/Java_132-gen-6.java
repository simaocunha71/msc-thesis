import java.util.*;
import java.lang.*;

class Solution {
    public boolean isNested(String string) {
        if (string.length() < 2) {
            return false;
        }
        int openCount = 0;
        int closeCount = 0;
        for (char c : string.toCharArray()) {
            if (c == '[') {
                openCount++;
            } else {
                closeCount++;
            }
            if (closeCount > openCount) {
                return true;
            }
        }
        return false;
    }
}