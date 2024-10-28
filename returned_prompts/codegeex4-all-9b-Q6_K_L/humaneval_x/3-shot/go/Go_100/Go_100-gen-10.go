    result := make([]int, n)
    count := 0
    for i:=0; i<n; i++{
        count += 2*i+1
        result[i] = count
    }
    return result
}

