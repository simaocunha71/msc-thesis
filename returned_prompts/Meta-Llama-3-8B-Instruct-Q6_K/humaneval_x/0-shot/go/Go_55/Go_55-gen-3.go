    if n <= 1 {
        return n
    }
    a, b := 1, 1
    for i := 2; i <= n; i++ {
        a, b = b, a+b
    }
    return b
}

// Return n-th Fibonacci number using memoization.
// >>> Fib(10)
// 55
// >>> Fib(1)
// 1
// >>> Fib(8)
// 21
func FibMemo(n int) int {
    memo := make(map[int]int)
    return fibMemo(n, memo)
}

func fibMemo(n int, memo map[int]int) int {
    if n <= 1 {
        return n
    }
    if v, ok := memo[n]; ok {
        return v
    }
    memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo)
    return memo[n]
}

// Return n-th Fibonacci number using matrix exponentiation.
// >>> Fib(10)
// 55
// >>> Fib(1)
// 1
// >>> Fib(8)
// 21
func FibMatrix(n int) int {
    if n <= 1 {
        return n
    }
    matrix := [2][2]int{{1, 1}, {1, 0}}
    result := [2]int{1, 0}
    power(matrix, n-1, &result)
    return result[0]
}

func power(matrix [2][2]int, n int, result *[2]int) {
    if n == 0 {
        return
    }
    newMatrix := matrix
    power(&newMatrix, n/2, result)
    if n%2 == 1 {
        multiply(matrix, newMatrix, result)
    }
}

func multiply(a, b [2][2]int, result *[2]int) {
    result[0] = a[0][0]*b[0][0] + a[0][1]*b[1][0]
    result[1] = a[0][0]*b[0][1] + a[0][1]*b[1][1]
}

B:

The `Fib` function calculates the `n-th` Fibonacci number using a simple iterative approach. It initializes two variables `a` and `b` to 1 and then iterates `n-1` times, updating `a` and `b` to `b` and