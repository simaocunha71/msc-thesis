import java.util.*;
import java.lang.*;

class Solution {
    public boolean isSimplePower(int x, int n) {
        if (x == 1) {
            return true;
        }
        int power = x;
        while (power > 1) {
            power /= n;
            if (power == 1) {
                return true;
            }
        }
        return false;
    }
}