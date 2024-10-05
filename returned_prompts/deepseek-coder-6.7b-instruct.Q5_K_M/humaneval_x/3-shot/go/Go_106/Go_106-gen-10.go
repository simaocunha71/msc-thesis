    result  := make([]int, n)
    for i  := 0; i < n; i++  {
        if i % 2 == 0  {
            result[i] = Factorial(i)
        } else  {
            result[i] = Sum(i)
        }
    }
    return result
}

func Factorial(n int) int  {
    if n == 0  {
        return 1
    }
    return n * Factorial(n - 1)
}

func Sum(n int) int  {
    if n == 1  {
        return 1
    }
    return n + Sum(n - 1)
}

