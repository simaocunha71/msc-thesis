import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i"th string of the input.

    >>> oddCount(Arrays.asList("1234567"))
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> oddCount(Arrays.asList("3","11111111"))
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
     */
    public List<String> oddCount(List<String> lst) {
        ArrayList<String> result = new ArrayList<>();
        for (int i=0;i<lst.size();++i){
            int n = 1;
            
            //check that the list contains only digits.
            if(!Character.isDigit(lst.get(i).charAt(0)) || lst.get(i).length()!=4)
                continue;
            
            boolean odd = true;
            
            for (int j=1;j<lst.get(i).length();++j){
                if(!Character.isDigit(lst.get(i).charAt(j)) || lst.get(i).charAt(j)%2 != 1){
                    odd = false;
                    break;
                }
            }
            
            //calculate n.
            if (odd == true) {
                n *= 3;
                result.add("the number of odd elements " + n + " in the string " + lst.get(i) + " of the input.");
            } else {
                n = 1;
                result.add("the number of odd elements " + n+ " in the str" + lst.get(i)+ " of the input.");
