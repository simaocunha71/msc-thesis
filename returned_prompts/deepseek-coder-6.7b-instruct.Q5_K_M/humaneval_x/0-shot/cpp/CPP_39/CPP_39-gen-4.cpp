    int fib(int n)
    {
        if (n <= 1)
           return n;
        return fib(n-1) + fib(n-2);
    }
    bool is_prime(int n)
    {
        if (n <= 1)
            return false;
        for (int i = 2; i*i <= n; i++)
        {
            if (n % i == 0)
                return false;
        }
        return true;
    }

B:
    int result = 0, i = 0;
    while(n > 0)
    {
        result = fib(i);
        if(is_prime(result))
        {
            n--;
        }
        i++;
    }
    return result;
}
```


## 4.2.3. Code Review

Here's a review of the code:

- The code starts with a definition of a function `prime_fib` that takes an integer argument `n`.
- Inside this function, two other functions are defined: `fib` and `is_prime`. The `fib` function calculates the n-th Fibonacci number, and the `is_prime` function checks whether a given number is prime.
- After these definitions, a loop is started. The loop continues until `n` is 0.
- Inside the loop, the `fib` function is called with increasing arguments. The result of this function call is stored in the `result` variable.
- After the `fib` function call, the `is_prime` function is called with the `result` variable as argument. If the `is_prime` function returns `true`, the value of `n` is decreased by 1.
- The loop continues until `n` is 0. At the end of the loop, the function returns the `result` variable. This is the n-th Fibonacci number that is also prime.


## 4.2.4. Complexity

This code has a complexity of O(n^2) because of the Fibonacci calculation and the prime check. The Fibonacci calculation is done in a recursive way, and for each call