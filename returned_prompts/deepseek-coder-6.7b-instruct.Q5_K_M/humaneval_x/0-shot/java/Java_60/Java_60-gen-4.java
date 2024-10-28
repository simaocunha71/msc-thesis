        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
}


A: 
Here is the corrected code:

import java.util.*;
import java.lang.*;

class Solution  {
    /**
    sumToN is a function that sums numbers from 1 to n.
    >>> sumToN(30)
    returns 465
    >>> sumToN(100)
    returns 5050
    >>> sumToN(5)
    returns 15
    >>> sumToN(10)
    returns 55
    >>> sumToN(1)
    returns 1
      */
    public int sumToN(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
}

In the question, the input and output examples were not in the form of a docstring, so I've added it as a comment to the function. The function now sums the numbers from 1 to the input integer n and returns the sum.

A: 
Here is the corrected code:

import java.util.*;
import java.lang.*;

class Solution  {
    /**
    sumToN is a function that sums numbers from 1 to n.
    >>> sumToN(30)
    returns 465
    >>> sumToN(100)
    returns 5050
    >>> sumToN(5)
    returns 15
    >>> sumToN(10)
    returns 55
    >>> sumToN(1)
    returns 1
      */
    public int sumToN(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
}

In the question, the input and output examples were not in the form of a docstring, so I've added it as a comment to the function.