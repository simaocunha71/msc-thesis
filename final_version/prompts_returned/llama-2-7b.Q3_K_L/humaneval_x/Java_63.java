import java.util.*;
import java.lang.*;

class Solution {
    /**
    The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
     */
    public int fibfib(int n) {
        if (n < 3) return 0;
        // I'd start by creating a Fibonacci Tree, but this is rather slow:
        // System.out.println("FibFib for " + n);
        // Map<Integer, Integer> fibMap = new HashMap<>();
        // for (int i=1; i<=n/2; i++) {
        //     fibMap.put(i, fibfib(i) + 2*fibfib(i-1));
        // }
        // if (!fibMap.containsKey(n/2)) return n/2 - 1;
        
        // In fact, I'd just make a Fibonacci Tree, but that's rather slow:
        // System.out.println("FibFib for " + n);
        // Map<Integer, Integer> fibMap = new HashMap<>();
        // LinkedList<Integer> fibList = new LinkedList<>();
        // fibList.add(0);
        // int index = 1;
        // while (index <= n) {
        //     int sum = 2*fibList.getLast() + 1;
        
        //     if (!fibMap.containsKey(sum)) fibMap.put(sum, new LinkedList<Integer>());
        
        //     // add the new node's value to its parent
        //