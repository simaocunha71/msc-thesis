    result := make([]int, n)

    for i := 0; i < n; i++ {
        if i % 2 == 0 {
            result[i] = i
        }else{
            result[i] = i+1
        }
    }
    return result
}



