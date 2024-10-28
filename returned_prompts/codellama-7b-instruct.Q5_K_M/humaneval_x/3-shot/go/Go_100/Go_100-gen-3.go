    result := make([]int, 0)
    for i := 1; i <= n; i++ {
        if i%2 == 0 {
            result = append(result, i+1)
        }else{
            result = append(result, i+2)
        }
    }
    return result
}



