        int sum1 = 0;
        int sum2 = 0;

        for(String s: lst1)
            sum1 += s.length();

        for(String s: lst2)
            sum2 += s.length();

        if(sum1 < sum2)
            return lst1;
        else if(sum1 > sum2)
            return lst2;
        else
            return lst1;
    }
}

The function calculates the total number of characters in lst1 and lst2 respectively and then compares these sums to determine which list has the smaller total number of characters. If the sum of lst1 is less than that of lst2, then it returns lst1. If the sum of lst2 is less than that of lst1, then it returns lst2. If the sums are equal, then it returns lst1 as per the question's requirement.
*/

import java.util.*;
import java.lang.*;

class Solution  {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        int sum1 = 0;
        int sum2 = 0;

        for(String s: lst1)
            sum1 += s.length();

        for(String s: lst2)
            sum2 += s.length();

        if(sum1 < sum2)
            return lst1;
        else if(sum1 > sum2)
            return lst2;
        else
            return lst1;
    }
}

//test
public class Main{
    public static void main(String[] args){
        Solution s = new Solution();

        System.out.println(s.totalMatch(Arrays.asList(), Arrays.asList())); //[]
        System.out.println(s.totalMatch(Arrays.asList("hi", "admin"), Arrays.asList("hI", "Hi"))); //["hI", "Hi"]
        System.out.println(s.totalMatch(Arrays.asList("hi", "admin"), Arrays.asList("hi", "hi", "admin", "