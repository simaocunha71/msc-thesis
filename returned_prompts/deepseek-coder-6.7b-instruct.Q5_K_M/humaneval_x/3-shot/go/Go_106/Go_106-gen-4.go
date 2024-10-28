    result := make([]int, n)

    for i := range result {
        if i % 2 == 0 {
            result[i] = Factorial(i)
        } else {
            result[i] = Sum(i + 1)
        }
    }

    return result
}

func Factorial(n int) int {
    if n == 0 || n == 1 {
        return 1
    }
    return n * Factorial(n - 1)
}

func Sum(n int) int {
    return n * (n + 1) / 2
}



