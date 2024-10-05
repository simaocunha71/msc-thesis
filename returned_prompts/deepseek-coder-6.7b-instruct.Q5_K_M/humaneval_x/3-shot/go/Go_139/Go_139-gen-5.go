    result := 1
    for i:=n; i>=1; i-- {
        result *= Factorial(i)
    }
    return result
}

func Factorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * Factorial(n-1)
}



