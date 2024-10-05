    result := make([]int, 0)

    for i := 1; i <= n; i++ {
        result = append(result, i+i%2)
    }

    return result
}



