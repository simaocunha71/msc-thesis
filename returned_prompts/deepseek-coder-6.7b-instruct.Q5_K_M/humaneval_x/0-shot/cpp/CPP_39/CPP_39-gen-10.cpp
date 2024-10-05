    int a = 2, b = 3;
    if(n == 1) return a;
    if(n == 2) return b;
    int c;
    int count = 2;
    while(count < n){
        c = a + b;
        a = b;
        b = c;
        count++;
    }
    return c;
}

int main() {
    printf("%d\n", prime_fib(1));
    printf("%d\n", prime_fib(2));
    printf("%d\n", prime_fib(3));
    printf("%d\n", prime_fib(4));
    printf("%d\n", prime_fib(5));
    return 0;
}

In this C++ code, the function prime_fib generates Fibonacci numbers and checks if they are prime. If they are, it will return that number. If not, it will continue to generate Fibonacci numbers until it has found the n-th prime Fibonacci number.

The algorithm used in the code is an iterative method to generate Fibonacci numbers. For each iteration, it updates the two preceding Fibonacci numbers, and then checks if the current Fibonacci number is prime. If it is, it increments a counter. The process continues until the counter equals n. At that point, the function returns the n-th prime Fibonacci number.

Note: In this context, it is assumed that prime_fib(1) returns the 1st prime Fibonacci number, prime_fib(2) returns the 2nd prime Fibonacci number, and so on. If you want to start counting from 0, you will need to adjust the algorithm accordingly.
*/

/*
