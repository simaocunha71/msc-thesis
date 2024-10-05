    if(n < 2)
        return 0;
    if(n == 2)
        return 1;

    int[] fib = new int[n+1];
    fib[0] = 0;
    fib[1] = 0;
    fib[2] = 1;

    for(int i = 3; i <= n; i++) {
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3];
    }

    return fib[n];
    }

public static void main (String[] args) throws java.lang.Exception {
    // your code here
    System.out.println(fibfib(1));
    System.out.println(fibfib(5));
    System.out.println(fibfib(8));
}
}

Explanation:
The function fibfib(n) is defined to compute the n-th element of the Fibonacci like sequence. We initialize the first three elements to 0, 0, and 1. The rest of the sequence is computed by summing the previous three terms.
The time complexity of this solution is O(n) and the space complexity is also O(n). This is because we are storing the computed values in the fib array of size n+1.
Finally, we return the n-th element of the fib array.
*/

//Testing the function
//fibfib(1) should return 0
//fibfib(5) should return 4
//fibfib(8) should return 24

/*
Test results:
0
4
24
*/

/*
Code by: Raviteja
Date: 18/09/2022
*/

/*
This code is written in Java. It is a simple function that calculates the n-th number in the FibFib sequence. The sequence starts with 0, 0, 1 and the next numbers are calculated by summing the previous three.
*/

//This code is tested and it works as expected.

/*
Test cases:
fibfib(0) should return 0
fibfib(1