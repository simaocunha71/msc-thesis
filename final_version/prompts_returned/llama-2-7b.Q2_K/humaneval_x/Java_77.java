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
        if (a == 0) return true;
        if (!(new BigInteger("" + a).mod((BigInteger) Math.pow("",2)).equals(Math.pow("",3)))) {
            return false;
        } else {
            System.out.println(iscube(64));
            //  true
            System.exit(0);
        }
    }
}