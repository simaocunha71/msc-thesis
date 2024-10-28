    result := make([]int, n)

    for i := 1; i <= n; i++ {
        if i % 2 == 0 {
            result[i-1] = factorial(i)
        } else {
            result[i-1] = sum_up_to_n(i)
        }
    }

    return result
}

func factorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * factorial(n-1)
}

func sum_up_to_n(n int) int {
    sum := 0
    for i := 1; i <= n; i++ {
        sum += i
    }
    return sum
}



