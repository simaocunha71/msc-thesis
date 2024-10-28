    result := make([]int, n)
    for i:=1; i<=n; i++ {
        if i % 2 == 0 {
            result[i-1] = Factorial(i)
        } else {
            result[i-1] = Sum(i)
        }
    }
    return result
}

func Factorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * Factorial(n-1)
}

func Sum(n int) int {
    sum := 0
    for i:=1; i<=n; i++ {
        sum += i
    }
    return sum
}


