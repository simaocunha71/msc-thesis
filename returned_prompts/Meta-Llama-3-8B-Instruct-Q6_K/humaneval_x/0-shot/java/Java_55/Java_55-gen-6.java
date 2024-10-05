    int fib(int n) {
        if(n <= 1) {
            return n;
        }
        int a = 0, b = 1, sum = 1;
        for(int i = 2; i <= n; i++) {
            sum = a + b;
            a = b;
            b = sum;
        }
        return sum;
    }

Solution explanation:
The solution is using the iterative approach to calculate the n-th Fibonacci number. The Fibonacci sequence is defined as: 
F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1.

We use a for loop to iterate from 2 to n, and in each iteration, we calculate the sum of the previous two numbers in the sequence (a and b), and update a and b for the next iteration. Finally, we return the sum as the n-th Fibonacci number.

The base case is when n <= 1, in which case we return n directly, since F(0) = 0 and F(1) = 1.

The time complexity of this solution is O(n), since we need to iterate n times to calculate the n-th Fibonacci number. The space complexity is O(1), since we only need a constant amount of space to store the variables a, b, and sum.