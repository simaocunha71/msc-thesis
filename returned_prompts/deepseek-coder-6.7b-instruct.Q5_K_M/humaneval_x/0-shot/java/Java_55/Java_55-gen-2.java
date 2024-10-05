        if (n <= 1)
            return n;
        int fib = 1;
        int prevFib = 1;

        for (int i = 2; i < n; i++) {
            int temp = fib;
            fib += prevFib;
            prevFib = temp;
        }
        return fib;
    }
}

The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. It usually starts with 0 and 1. In this case, the function `fib` is a simple way to calculate the nth number in the Fibonacci sequence.

The function uses a loop to calculate the Fibonacci sequence, storing the last two numbers as well as the current one. The first two numbers in the Fibonacci sequence are 1, so if n is 1 or less, the function will return n itself.

In the loop, the current Fibonacci number is calculated by adding the two previous Fibonacci numbers. The previous Fibonacci number is stored in a temporary variable before it is updated. This way, the loop keeps track of the last two Fibonacci numbers.

Finally, the current Fibonacci number is returned.
*/

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.fib(10)); // 55
        System.out.println(sol.fib(1)); // 1
        System.out.println(sol.fib(8)); // 21
    }
}


































































































































