    if n <= 1 {
        return n
    }
    // This is where the magic happens
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
    a, b := 1, 1
    for i := 2; i <= n; i++ {
        a, b = b, a+b
    }
    return b
}

C:
    if n <= 1 {
        return n
    }
    a, b := 0, 1
    for i := 2; i < n; i++ {
        a, b = b, a+b
    }
    return b
}

D:
    if n <= 1 {
        return n
    }
    a, b := 1, 1
    for i := 1; i < n; i++ {
        a, b = b, a+b
    }
    return b
}

The correct answer is B:

// Return n-th Fibonacci number.
// >>> Fib(10)
// 55
// >>> Fib(1)
// 1
// >>> Fib(8)
// 21
func Fib(n int) int {

    if n <= 1 {
        return n
    }
    a, b := 1, 1
    for i := 2; i <= n; i++ {
        a, b = b, a+b
    }
    return b
} 

The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it. Starting with 0 and 1, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.

The function `Fib(n)` returns the nth Fibonacci number. If `n` is 1 or less, it returns `n` because the sequence starts with 0 and 1. If `n` is greater than 1, it uses a loop to calculate the Fibonacci number. In the loop, it uses two variables `a` and `b` to keep track of the last two numbers in the sequence. In each iteration, it updates `a` and `b` to be `b