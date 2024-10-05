```go
func F(n int) []int {
    if n < 1 {
        return []int{}
    }
    result := make([]int, n)
    for i := 1; i <= n; i++ {
        if i%2 == 0 {
            result[i-1] = factorial(i)
        } else {
            result[i-1] = sumTo(i)
        }
    }
    return result
}

func factorial(n int) int {
    if n == 0 {
        return 1
    }
    result := 1
    for i := 1; i <= n; i++ {
        result *= i
    }
    return result
}

func sumTo(n int) int {
    return n * (n + 1) / 2
}
```