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
        if (lst1 == null || lst2 == null) return "NULL PARAMETER IN LIST";
        int evenEle = 0;
        
        for (int element : lst1) {
            evenEle += (element % 2);
        }
        
        // check if sum of all elements in first list is odd or even.
        if (evenEle != 0 && evenEle % 2 == 1) {
            return "NO";
        } else {
            for(int element : lst2) {
                evenEle += element;
            }
            
            // check again, this time in the second list.
            if (evenEle != 0 && evenEle % 2 == 1) {
                return "NO";
            } else {
                return "YES";
            }
        }
    }
}