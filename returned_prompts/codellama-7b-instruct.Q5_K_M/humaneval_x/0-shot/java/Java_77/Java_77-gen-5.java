import java.util.*;
import java.lang.*;

class Solution {
    public boolean iscube(int a) {
        int root = (int) Math.pow(a, 1.0/3);
        return a == root*root*root;
    }
}
