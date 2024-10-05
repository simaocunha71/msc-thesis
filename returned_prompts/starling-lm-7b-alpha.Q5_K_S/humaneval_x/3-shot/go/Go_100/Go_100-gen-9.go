    result := make([]int, n)
    result[n-1] = n
    for i := n-2; i >= 0; i-- {
        if n&1 == 0 {
            result[i] = result[i+1] + 2
        }else {
            result[i] = result[i+1] + 1
        }
    }
    return result
}



