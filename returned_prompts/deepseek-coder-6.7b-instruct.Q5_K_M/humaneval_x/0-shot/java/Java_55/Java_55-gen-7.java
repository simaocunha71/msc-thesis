        if(n <= 1){
            return n;
        }
        int fib1 = 0;
        int fib2 = 1;
        int fib3 = 0;
        for(int i = 2; i <= n; i++){
            fib3 = fib1 + fib2;
            fib1 = fib2;
            fib2 = fib3;
        }
        return fib3;
    }
}

This solution uses iterative method to find n-th Fibonacci number. It initializes first two numbers of Fibonacci sequence to 0 and 1 and then it calculates next Fibonacci number as a sum of previous two. It does this for n times. 
The time complexity of this solution is O(n) and space complexity is O(1).

Please, note that you should provide test cases to check your solution.

Also, ensure that your solution works with edge cases, like when n = 0 or n = 1.
*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.fib(10));
        System.out.println(solution.fib(1));
        System.out.println(solution.fib(8));
    }
}

//src/main/java/com/example/demo/FibonacciRecursive.java
package com.example.demo;

/*
