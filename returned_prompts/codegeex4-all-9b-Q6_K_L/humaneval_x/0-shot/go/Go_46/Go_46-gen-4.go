func Fib4(n int) int {
    if n < 4 {
        switch n {
        case 0:
            return 0
        case 1:
            return 0
        case 2:
            return 2
        case 3:
            return 0
        default:
            return 0
        }
    }

    fib := make([]int, n+1)
    fib[0] = 0
    fib[1] = 0
    fib[2] = 2
    fib[3] = 0

    for i := 4; i <= n; i++ {
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4]
    }

    return fib[n]
}

// Time complexity: O(n)
// Space complexity: O(n)

// Test cases:
// Fib4(5) -> 4
// Fib4(6) -> 8
// Fib4(7) -> 14