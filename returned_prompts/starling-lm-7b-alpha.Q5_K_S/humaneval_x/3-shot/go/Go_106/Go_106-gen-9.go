    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i%2 == 0 {
            result[i] = math.Factorial(i)
        }else{
            result[i] = SumNumbers(i)
        }
    }
    return result
}

func SumNumbers(n int) int {
    if n == 0 {
        return 0
    }else {
        return n + SumNumbers(n-1)
    }
}



