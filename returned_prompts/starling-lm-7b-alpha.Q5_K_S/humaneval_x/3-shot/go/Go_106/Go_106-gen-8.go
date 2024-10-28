    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i % 2 == 0 {
            result[i] = math.Factorial(i)
        } else {
            result[i] = Sum(i)
        }
    }
    return result
}

func Sum(n int) int {
    result := 0
    for i := 1; i <= n; i++ {
        result += i
    }
    return result
}

func math.Factorial(n int) int {
    result := 1
    for i := 1; i <= n; i++ {
        result *= i
    }
    return result
}




