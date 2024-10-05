func Fib4(n int) int {
    a, b, c, d, e := 0, 0, 2, 0, 0
    for i := 4; i <= n; i++ {
        a, b, c, d, e = b, c, d, e, a+b+c+d
    }
    return e
}