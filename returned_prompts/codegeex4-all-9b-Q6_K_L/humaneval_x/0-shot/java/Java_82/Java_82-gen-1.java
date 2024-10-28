import java.util.*;
import java.lang.*;

class Solution {
    public boolean primeLength(String string) {
        int length = string.length();
        if (length <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(length); i++) {
            if (length % i == 0) {
                return false;
            }
        }
        return true;
    }
}