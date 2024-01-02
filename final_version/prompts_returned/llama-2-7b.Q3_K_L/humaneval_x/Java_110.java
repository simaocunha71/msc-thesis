import java.util.*;
import java.lang.*;

class Solution {
    /**
    In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange(Arrays.asList(1, 2, 3, 4), Arrays.asList(1, 2, 3, 4)) => "YES"
    exchange(Arrays.asList(1, 2, 3, 4), Arrays.asList(1, 5, 3, 4)) => "NO"
    It is assumed that the input lists will be non-empty.
     */
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        // Your code here
        boolean even1 = true;
        while (even1 && !lst1.isEmpty()) {
            if (!even1){
                int tmp = lst2.get(0);
                lst2.remove(0);
                lst1.add(tmp);
            }else{
                for (int i= 1; i< lst1.size();i++){
                    if(!(lst1.get(i) % 2 == 0)) {
                        lst1.set(i, lst1.get(i) - 1);
                        even1 = false;
                    }
                }
            }
        }
        return (even1)? "YES":"NO";
    }
}
