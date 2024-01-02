import java.util.*;
import java.lang.*;

class Solution {
    /**
    You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
     */
    public int sumSquares(List<Double> lst) {
        //Write your code here
        double sum=0;
        
	for (int i=0;i<=lst.size()-1;++i){
		if ((i%2==0)&&(Math.pow((double)(lst.get(i)), 2)-Math.pow(lst.get(i), 2)>Math.EPS)) {sum+=Math.pow((double)(lst.get(i)), 2);}
		if ((i%2!=0)&&(Math.pow((double)(lst.get(i)), 2)-Math.pow(lst.get(i), 2)>Math.EPS)) {sum+=Math.pow((double)(lst.get(i)), 2);}
            sum+=(Math.pow((double)(lst.get(i)), 2));
        }
         return Math.round(sum*100)/100;
    }
    
}
