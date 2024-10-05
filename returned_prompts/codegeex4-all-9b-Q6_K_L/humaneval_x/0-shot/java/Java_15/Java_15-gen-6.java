import java.util.*;
import java.lang.*;

class Solution {
    public String stringSequence(int n) {
        String result = "";
        for(int i = 0; i <= n; i++) {
            result += i + " ";
        }
        return result.trim();
    }
}