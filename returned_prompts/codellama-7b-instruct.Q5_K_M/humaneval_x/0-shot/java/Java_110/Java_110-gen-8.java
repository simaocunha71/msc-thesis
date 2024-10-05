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
        //Write your code here
        //If the list is empty, return "YES"
        if(lst1.size() == 0 || lst2.size() == 0)
            return "YES";

        //Create two lists of even numbers and one list of odd numbers
        List<Integer> evenLst = new ArrayList<Integer>();
        List<Integer> oddLst = new ArrayList<Integer>();

        //Iterate through both lists
        for(int i = 0; i < lst1.size(); i++)
        {
            //If the number is even, add it to the even list
            if(lst1.get(i) % 2 == 0)
                evenLst.add(lst1.get(i));
            //If the number is odd, add it to the odd list
            else
                oddLst.add(lst1.get(i));
        }

        //Iterate through both lists
        for(int i = 0; i < lst2.size(); i++)
        {
            //If the number is even, add it to the even list