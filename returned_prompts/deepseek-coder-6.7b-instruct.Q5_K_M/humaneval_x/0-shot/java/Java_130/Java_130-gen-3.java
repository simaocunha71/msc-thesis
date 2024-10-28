        List<Integer> list = new ArrayList<>();
        if(n<0) throw new IllegalArgumentException("n should be non-negative");
        if(n>=0) list.add(3);
        if(n>=1) list.add(2);
        if(n>=2) list.add(8);

        for(int i=3; i<=n; i++){
            int next;
            if(i%2==0) next = list.get(i-1)+1;
            else next = list.get(i-1)+list.get(i-2)+list.get(i+1);
            list.add(next);
        }

        return list;
    }
}


A: Your algorithm seems correct, but it will throw an exception when you try to access an element at index i+1 that does not exist in the list. You should initialize your list with a size of n+1, and then fill the list with the Tribonacci sequence. 
Here is the corrected code:
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> tri(int n) {
        if(n<0) throw new IllegalArgumentException("n should be non-negative");

        List<Integer> list = new ArrayList<>(Collections.nCopies(n+1, 0));
        if(n>=0) list.set(0, 3);
        if(n>=1) list.set(1, 2);
        if(n>=2) list.set(2, 8);

        for(int i=3; i<=n; i++){
            int next;
            if(i%2==0) next = list.get(i-1)+1;
            else next = list.get(i-1)+list.get(i-2)+list.get(i-3);
            list.set(i, next);
        }

        return list;
    }
}

This code initializes the list with 0s and then sets the correct values at the correct indices.

A: Here is a Python solution using memoization to optimize the runtime