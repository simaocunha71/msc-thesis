import java.util.*;
import java.lang.*;

class Solution {
    public boolean simplify(String x, String n) {
        String[] xy = x.split("/");
        String[] ny = n.split("/");
        if(xy[1].equals(ny[1])){
            return true;
        }else{
            return false;
        }
    }
}
