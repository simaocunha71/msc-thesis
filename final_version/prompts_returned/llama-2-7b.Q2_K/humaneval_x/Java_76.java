import java.util.*;
import java.lang.*;

class Solution {
    /**
    Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    isSimplePower(1, 4) => true
    isSimplePower(2, 2) => true
    isSimplePower(8, 2) => true
    isSimplePower(3, 2) => false
    isSimplePower(3, 1) => false
    isSimplePower(5, 3) => false
     */
    public boolean isSimplePower(int x, int n) {
        if (x == 0 || x < 0 ) return true;
        
        int power = BigInteger.valueOf(n).pow((long)(Math.log10(Math.abs(x))));
        BigInteger b = new BigInteger(power.toString());
        while (b.mod(1L) != 1L && !b.equals(BigInteger.ZERO)) {
            int c;
            try {
                c = Integer.parseInt(b.toString()) + 1;
            } catch (Exception e) {}
            if (c == 1) { // we have a solution, so it's not simple
                return false;
            } else {
                b = new BigInteger(String.valueOf(c));
            }
        }
        b = x * b;
        while (!b.equals(BigInteger.ZERO) && !new BigInteger(1L).equals(b)) {
            int c = Integer.parseInt(String.valueOf(b.mod(1L))) + 1;
             try { // we have a solution, so it's not simple
                if (c == 1)
                    return false;
            } catch (Exception e) {}
         b = new BigInteger(String.valueOf(c));
        }
        return true;
    }
}
