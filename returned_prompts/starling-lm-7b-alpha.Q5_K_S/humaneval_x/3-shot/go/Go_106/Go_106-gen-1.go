    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i % 2 == 0 {
            result[i] = math.Factorial(i)
        }else {
            result[i] = CalcSumOfNumbers(i)
        }
    }
    return result
}

func CalcSumOfNumbers(n int) int {
    return n * (n + 1) / 2
}

func math.Factorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * math.Factorial(n - 1)
}



