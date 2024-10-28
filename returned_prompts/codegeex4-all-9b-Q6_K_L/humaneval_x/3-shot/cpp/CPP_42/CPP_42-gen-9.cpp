func Fib4(n int) int {
    if n == 0 {
        return 0
    } else if n == 1 {
        return 0
    } else if n == 2 {
        return 2
    } else if n == 3 {
        return 0
    } else {
        return Fib4(n-1) + Fib4(n-2) + Fib4(n-3) + Fib4(n-4)
    }
}