    result := make([]int, 0)
    if n == 0 {
        return result
    }
    result = append(result, 1)
    for i := 2; i <= n; i++ {
        if i%2 == 0 {
            result = append(result, factorial(i))
        } else {
            result = append(result, sum(i))
        }
    }
    return result
}

func factorial(n int) int {
    if n == 1 {
        return 1
    }
    return n * factorial(n-1)
}

func sum(n int) int {
    result := 0
    for i := 1; i <= n; i++ {
        result += i
    }
    return result
}



