    if n <= 1 {
        return n
    }
    a, b := 0, 1
    for i := 2; i <= n; i++ {
        a, b = b, a+b
    }
    return b
}

B:
    if n <= 1 {
        return n
    }
    return fib(n-1) + fib(n-2)
}

C:
    if n <= 1 {
        return n
    }
    return fib(n-1) + fib(n-1)
}

D:
    if n <= 1 {
        return n
    }
    return fib(n-2) + fib(n-1)
}

E:
    if n <= 1 {
        return n
    }
    return fib(n-3) + fib(n-2)
}

F:
    if n <= 1 {
        return n
    }
    return fib(n-1) - fib(n-2)
}

G:
    if n <= 1 {
        return n
    }
    return fib(n-2) - fib(n-1)
}

Which one is correct?

A) A: The iterative approach

Explanation: The Fibonacci sequence is defined as follows: F(n) = F(n-1) + F(n-2). To find the nth Fibonacci number, we can use an iterative approach. The function takes an integer n as input and returns the nth Fibonacci number.

B) B: The recursive approach

Explanation: This is not the correct answer. The recursive approach is not efficient for large values of n, as it does a lot of repeated computation.

C) C: The recursive approach with identical recursive calls

Explanation: This is not the correct answer. The recursive approach with identical recursive calls is not efficient for large values of n, as it does a lot of repeated computation.

D) D: The recursive approach with identical recursive calls

Explanation: This is not the correct answer. The recursive approach with identical recursive calls is not efficient for large values of n, as it does a lot of repeated computation.

E) E: The recursive approach with identical recursive calls

Explanation: This is not the correct answer. The recursive approach with identical recursive calls is not efficient for large values of n, as it does a lot of repeated computation.

F) F: The recursive approach with identical recursive calls

Explanation: This is not the correct answer. The recursive approach with identical recursive calls is not efficient for large values of n, as it does