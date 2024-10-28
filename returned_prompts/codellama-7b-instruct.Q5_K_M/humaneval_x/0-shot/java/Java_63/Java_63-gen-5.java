import java.util.*;
import java.lang.*;

class Solution {
    public int fibfib(int n) {
        if (n <= 2) {
            return n;
        } else {
            return fibfib(n-1) + fibfib(n-2) + fibfib(n-3);
        }
    }
}
