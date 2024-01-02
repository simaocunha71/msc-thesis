import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> stringSequence(0)
    "0"
    >>> stringSequence(5)
    "0 1 2 3 4 5"
     */
    public String stringSequence(int n) {
        //Write your code here
        StringBuilder sb = new StringBuilder();
        
       for (int i=0;i<n ;i++){
           if(sb.length()==0){
               sb.append("0");
            }else{
                sb.append(" ");
            }
           sb.append(i);
        }   
      return sb.toString();

      
    }
}