import java.util.*;
import java.lang.*;

class Solution {
    public int chooseNum(int x, int y) {
        int max = Math.max(x, y);
        int min = Math.min(x, y);
        if(max%2==0){
            if(min%2==0)
                return max;
            else
                return max-1;
        }
        else
            return -1;
    }
}
