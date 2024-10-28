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

        // Write your code here
        int l1 = lst1.size();
        int l2 = lst2.size();
        int[] count = new int[l2];

        for(int i = 0; i < l1; i++) {
            if(lst1.get(i) % 2 == 0) {
                for(int j = 0; j < l2; j++) {
                    if(lst2.get(j) % 2 == 0) {
                        count[j]++;
                    }
                }
            }
        }

        for(int i = 0; i < l2; i++) {
            if(count[i] == 0) {
                return "NO";
            }
        }

        return "YES";
    }
}
