    if (n <= 1)
        return n;
    else
        return fib(n-1) + fib(n-2);
}

int main() {
   int n;
   printf("Enter a positive integer: ");
   scanf("%d",&n);
   printf("Fibonacci number = %d", fib(n));
   return 0;
}




A: 
I've written a program in C++ to solve the problem. The program takes an integer input n from the user and then calculates the n-th Fibonacci number. It uses recursion to calculate the Fibonacci numbers.

The program starts by checking if the input number n is less than or equal to 1. If it is, the program returns n because the n-th Fibonacci number is n itself.

If the input number n is greater than 1, the program calls itself twice with the arguments n-1 and n-2. This is known as recursion and is used to calculate the n-th Fibonacci number.

The recursive calls will eventually reach the base case of the Fibonacci sequence (0 and 1) and start adding up the numbers.

The final result is the n-th Fibonacci number.

Here is the C++ code:

```cpp
#include<iostream>
using namespace std;
int fib(int n){
   if (n <= 1)
      return n;
   else
      return fib(n-1) + fib(n-2);
}
int main() {
   int n;
   cout << "Enter a positive integer: ";
   cin >> n;
   cout << "Fibonacci number = " << fib(n);
   return 0;
}
```

This program will work correctly for small values of n but may take a long time for larger values due to the exponential time complexity of the recursive solution. For larger values of n, a more efficient solution would be to use an iterative approach or memoization to store and retrieve previously calculated values, reducing the number of redundant calculations.

In summary, this program calculates the n-th Fibonacci number by recursively