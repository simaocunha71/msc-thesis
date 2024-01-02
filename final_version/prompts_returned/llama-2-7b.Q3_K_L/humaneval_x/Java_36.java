import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizzBuzz(50)
    0
    >>> fizzBuzz(78)
    2
    >>> fizzBuzz(79)
    3
     */
    public int fizzBuzz(int n) {
        // TODO: Write your code here.
        ArrayList<Integer> list=new ArrayList<>();
        for (int i = 0; i < n; ++i) {
            if((i+1)/2%3==0){
                list.add(0);
            }else if((i/11)%2 ==0 && ((i + 1)/11) % 3 == 0 ){
                    list.add(1);
            }else{
                list.add(45-i);
            }
        }
        for (int i : list){
            System.out.print(i+" ");
        }
        return list.size();
    }
}
