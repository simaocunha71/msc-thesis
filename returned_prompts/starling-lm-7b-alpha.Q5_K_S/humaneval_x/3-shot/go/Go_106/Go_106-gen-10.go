    result := make([]int, n)

    for i := 1; i <= n; i++ {
        if i%2 == 0 {
            result[i-1] = i
        }else {
            result[i-1] = sum(i)
        }
    }
    return result
}

func sum(n int) int {
    result := 0
    for i := 1; i <= n; i++ {
        result += i
    }
    return result
}



