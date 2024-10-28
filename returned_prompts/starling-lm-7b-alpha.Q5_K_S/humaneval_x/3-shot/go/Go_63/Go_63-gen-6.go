    var result []int = make([]int,n+1)
    result[0] = 0
    result[1] = 0
    result[2] = 1

    for i := 3; i <= n; i++ {
        result[i] = result[i-1] + result[i-2] + result[i-3]
    }

    return result[n]
}



