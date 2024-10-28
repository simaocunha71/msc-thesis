import java.util.*;
import java.lang.*;

class Solution {
    public boolean simplify(String x, String n) {
        // Write your code here
        int x1 = Integer.parseInt(x.split("/")[0]);
        int x2 = Integer.parseInt(x.split("/")[1]);
        int n1 = Integer.parseInt(n.split("/")[0]);
        int n2 = Integer.parseInt(n.split("/")[1]);
        if(x1 * n2 == n1 * x2) return true;
        else return false;
    }
}



