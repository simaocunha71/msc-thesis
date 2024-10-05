// There are two major ways to solve this problem. The first is to use recursion and the second is to use dynamic programming.
//
// The recursive method is simple, but it is not efficient because it will calculate the same Fibonacci numbers multiple times.
//
// The dynamic programming method is more efficient because it will only calculate each Fibonacci number once.
//
// Here is the recursive solution:

func Fib(n int) int {
    if n <= 0 {
        return 0
    } else if n == 1 {
        return 1
    } else {
        return Fib(n-1) + Fib(n-2)
    }
}

// And here is the dynamic programming solution:

func Fib(n int) int {
    if n <= 0 {
        return 0
    } else if n == 1 {
        return 1
    } else {
        fib := make([]int, n+1)
        fib[1] = 1
        for i := 2; i <= n; i++ {
            fib[i] = fib[i-1] + fib[i-2]
        }
        return fib[n]
    }
}
