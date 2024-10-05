import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a list of positive integers x. return a sorted list of all
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> uniqueDigits(Arrays.asList(15, 33, 1422, 1))
    [1, 15, 33]
    >>> uniqueDigits(Arrays.asList(152, 323, 1422, 10))
    []
     */
    public List<Integer> uniqueDigits(List<Integer> x) {

        List<Integer> result = new ArrayList<>();
        for(int i=0; i<x.size(); i++){
            int num = x.get(i);
            if(num%2==1){
                result.add(num);
            }
        }
        return result;
    }
}

B:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a list of positive integers x. return a sorted list of all
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> uniqueDigits(Arrays.asList(15, 33, 1422, 1))
    [1, 15, 33]
    >>> uniqueDigits(Arrays.asList(152, 323, 1422, 10))
    []
     */
    public List<Integer> uniqueDigits(List<Integer> x) {

        List<Integer> result = new ArrayList<>();
        for(int i=0; i<x.size(); i++){
            int num = x.get(i);
            if(num%2!=0){
                result.add(num);
            }
        }
        return result;
    }
}

C:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given