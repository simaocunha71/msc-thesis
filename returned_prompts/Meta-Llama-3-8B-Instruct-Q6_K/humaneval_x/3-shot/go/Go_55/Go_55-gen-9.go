    if n <= 1 {
        return n
    }
    a, b := 0, 1
    for i := 2; i <= n; i++ {
        a, b = b, a+b
    }
    return b
}
// or
func Fib(n int) int {
    if n <= 1 {
        return n
    }
    return fibHelper(n)
}

func fibHelper(n int) int {
    if n <= 1 {
        return n
    }
    return fibHelper(n-1) + fibHelper(n-2)
}
// or
func Fib(n int) int {
    if n <= 1 {
        return n
    }
    fib := [2]int{0, 1}
    for i := 2; i <= n; i++ {
        fib[i%2] = fib[(i-1)%2] + fib[(i-2)%2]
    }
    return fib[n%2]
}
// or
func Fib(n int) int {
    if n <= 1 {
        return n
    }
    fib := make([]int, n+1)
    fib[0] = 0
    fib[1] = 1
    for i := 2; i <= n; i++ {
        fib[i] = fib[i-1] + fib[i-2]
    }
    return fib[n]
}