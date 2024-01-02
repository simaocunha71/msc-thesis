import java.util.*;
import java.lang.*;

class Solution {
    /**
    sumToN is a function that sums numbers from 1 to n.
    >>> sumToN(30)
    465
    >>> sumToN(100)
    5050
    >>> sumToN(5)
    15
    >>> sumToN(10)
    55
    >>> sumToN(1)
    1
     */
    public int sumToN(int n) {
        // Your code here
        int sum = 0;
        
         for (int i=1;i<n+1;i++){
            if((i%3==0)&&(i%5==0))
                sum+=i;
            
            else if((i%3!=0) &&(i%5==0)){
            sum+=2*i;
        }else{
        	sum++;
            }
        
    	}
      return  sum;
    }
    
}