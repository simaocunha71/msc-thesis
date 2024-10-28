        if(n < 0) {
            throw new IllegalArgumentException("n must be >= 0");
        }
        if(n == 0 || n == 1) {
            return 0;
        }
        if(n == 2) {
            return 1;
        }
        int[] fib = new int[n+1];
        fib[0] = 0;
        fib[1] = 0;
        fib[2] = 1;
        for(int i = 3; i <= n; i++) {
            fib[i] = fib[i-1] + fib[i-2] + fib[i-3];
        }
        return fib[n];
    }
}

This program uses dynamic programming to compute the n-th fibfib number in O(n) time.

It first initializes the first three elements of the sequence in an array. Then, it iteratively computes the next elements of the sequence by summing the previous three elements. The result is stored in the array at the corresponding index, and the value of the n-th fibfib number is returned at the end.
*/

/*
R:
The code works by creating an array of size n+1 to store the FibFib sequence. The first three elements are initialized as 0, 0, and 1 respectively. The rest of the sequence is then computed by summing the previous three elements, and this value is stored in the array. The function finally returns the n-th element of the sequence.

The time complexity of this code is O(n), and the space complexity is O(n) because of the array used to store the sequence. This makes it more efficient than a naive recursive solution, which would have a time complexity of O(3^n) and a space complexity of O(n) due to the repeated computations of the same subproblems.

The code also includes a check for negative values of n, throwing an IllegalArgumentException if n is less than 0. This is to handle invalid input and prevent potential errors.
*/

/*
E:
Here is a sample run of the code:
>>> fibfib(1)
0
>>> fibfib(5)
4
>>> fibfib(8)
24
This output matches the