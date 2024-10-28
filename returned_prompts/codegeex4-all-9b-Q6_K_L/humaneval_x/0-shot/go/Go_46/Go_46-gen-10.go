func Fib4(n int) int {
    // Handle special cases
    if n < 0 {
        return -1
    }
    if n == 0 || n == 1 {
        return 0
    }
    if n == 2 {
        return 2
    }

    // Initialize the first four elements of the sequence
    a, b, c, d := 0, 0, 2, 0

    // Compute the sequence iteratively
    for i := 3; i <= n; i++ {
        a, b, c, d = b, c, d, a+b+c+d
    }

    return d
}