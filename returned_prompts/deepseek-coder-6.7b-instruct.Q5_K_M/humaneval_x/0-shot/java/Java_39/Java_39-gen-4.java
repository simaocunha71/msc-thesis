        int count = 0, fib1 = 0, fib2 = 1, fib = 0;
        while(count < n) {
            fib = fib1 + fib2;
            if(isPrime(fib)) count++;
            fib1 = fib2;
            fib2 = fib;
        }
        return fib;
    }

    public boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i * i <= n; i += 2)
            if (n % i == 0) return false;
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.primeFib(1)); // 2
        System.out.println(s.primeFib(2)); // 3
        System.out.println(s.primeFib(3)); // 5
        System.out.println(s.primeFib(4)); // 13
        System.out.println(s.primeFib(5)); // 89
    }
}
```

The program generates Fibonacci numbers and checks if they are prime. If a number is prime, it increments the count variable. When the count equals the input n, it returns the n-th Fibonacci number that is also prime.

The isPrime function checks if a number is prime by dividing it by all numbers up to its square root. If any of the divisions result in a remainder of zero, the number is not prime. Otherwise, it is prime.

In the main function, the program tests the primeFib function with several inputs.

This program uses a while loop to generate Fibonacci numbers and a for loop to check if they are prime. The time complexity of the program is O(n^1.5), where n is the input to the primeFib function.

This solution is correct because it generates Fibonacci numbers and checks if they are prime in the correct order. The primeFib function returns the n-th Fib