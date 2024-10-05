    if n <= 1 {
        return n
    }
    // 1. Fibonacci sequence is defined recursively as: 
    // F(n) = F(n-1) + F(n-2)
    // F(1) = 1, F(0) = 0
    // We will calculate F(n) by calculating F(n-1) and F(n-2)
    // First, we calculate F(n-1)
    prev := Fib(n - 1)
    // Then, we calculate F(n-2)
    prev2 := Fib(n - 2)
    // Now we have F(n-1) and F(n-2) so we can calculate F(n)
    return prev + prev2
}

B:
    if n <= 1 {
        return n
    }
    prev, prev2 := 1, 0
    for i := 2; i <= n; i++ {
        prev, prev2 = prev2, prev+prev2
    }
    return prev
}

C:
    if n <= 1 {
        return n
    }
    a, b := 1, 0
    for i := 2; i <= n; i++ {
        a, b = b, a+b
    }
    return a
}

D:
    if n <= 1 {
        return n
    }
    a, b := 1, 1
    for i := 2; i <= n; i++ {
        a, b = b, a+b
    }
    return b
}

E:
    if n <= 1 {
        return n
    }
    a, b := 1, 1
    for i := 2; i < n; i++ {
        a, b = b, a+b
    }
    return a + b

F:
    if n <= 1 {
        return n
    }
    a, b := 1, 1
    for i := 3; i <= n; i++ {
        a, b = b, a+b
    }
    return b

G:
    if n <= 1 {
        return n
    }
    a, b := 1, 1
    for i := 2; i <= n; i++ {
        a, b = b, a+b
    }
    return a

H:
    if n <= 1 {
        return n