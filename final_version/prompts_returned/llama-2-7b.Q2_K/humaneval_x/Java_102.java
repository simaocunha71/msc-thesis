import java.util.*;
import java.lang.*;

class Solution {
    /**
    This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If
    there's no such number, then the function should return -1.
    
    For example:
    chooseNum(12, 15) = 14
    chooseNum(13, 12) = -1
     */
    public int chooseNum(int x, int y) {
        // Your code here
        if (x == Integer.MIN_VALUE || !(y >= x)) {
            return Integer.MIN_VALUE;
        } else if(x <= 0 && x > y){
            return -1;
        }else{
            int maxEven = y-1, minNums=maxEven*2+1;
            for (int i = x ; i <= maxEven;i++){
                if ((maxEven%2) && i==maxEven){
                    return i;
                }
            }
        }
        
    
    System.out.println("chooseNum(1, 3) returns "+chooseNum(1, 3));
    System.out.println("chooseNum(-2, -4) returns "+chooseNum(-2,-4));    
        
    return -1;
}
public static void main(String[] args) {
        new Solution().chooseNum(-1000,-1);
   }

}