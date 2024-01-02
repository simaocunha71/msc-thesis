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
        if (x == 0 || n==0){ return true;}
        
        for (int i = 2; i*i <= n; i++)
            if (n%i == 0 && Math.pow(n, i) == x){
                System.out.println("found: "+i+" is a root of "+x);
                return true;
            }
        else{System.out.println("could not find: "+x+" is a root of "+n);}
        
        return false;
    }
    
    public static void main(String[] args) {
         Solution sol = new Solution();
         System.out.println(sol.isSimplePower(4, 2)); //true
         System.out.println(sol.isSimplePower(8, 2)); //true
         System.out.println(sol.isSimplePower(3, 2)); //false
         System.out.println(sol.isSimplePower(5, 3)); //false  
         System.out.println(sol.isSimplePower(4, 1)); //false
    }
}
