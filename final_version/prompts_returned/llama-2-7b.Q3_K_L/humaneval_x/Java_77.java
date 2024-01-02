import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that takes an integer a and returns true
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> true
    iscube(2) ==> false
    iscube(-1) ==> true
    iscube(64) ==> true
    iscube(0) ==> true
    iscube(180) ==> false
     */
    public boolean iscube(int a) {
        if (a < 0 || a > 216)
            return false;
        int i = 0;
        for (int j=1; j <= a; j++) {
            while ((i + j - 1) % j != 0 ) {
                i++;
            }
        }
        
        if(a == i*i*i || a==(int)(Math.sqrt(3)*i*i*i))return true;
        return false;
    }
}