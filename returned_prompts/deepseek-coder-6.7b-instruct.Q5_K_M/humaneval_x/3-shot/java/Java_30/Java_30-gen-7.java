        return l.stream().filter(i -> i > 0).collect(Collectors.toList());
     }
}


A: You are missing the import of java.util.stream.Collectors. Also, the return type of the function should be a List of Integer instead of List of int. Here is the correct code:

import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    
    /**
    Return only positive numbers in the list.
    >>> getPositive(Arrays.asList(-1, 2, -4, 5, 6))
    [2, 5, 6]
    >>> getPositive(Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10))
    [5, 3, 2, 3, 9, 123, 1]
    */
    public List<Integer> getPositive(List<Integer> l) {

    return l.stream().filter(i -> i > 0).collect(Collectors.toList());
    }
}


A: Your code seems correct except for the missing import of java.util.stream.Collectors. Here is the corrected version:

import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    
    /**
    Return only positive numbers in the list.
    >>> getPositive(Arrays.asList(-1, 2, -4, 5, 6))
    [2, 5, 6]
    >>> getPositive(Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10))
    [5, 3, 2, 3, 9, 123, 1]
    */
    public List<Integer> getPositive(List<Integer> l) {

    return l.stream().filter(i -> i > 0).collect(Collectors.toList