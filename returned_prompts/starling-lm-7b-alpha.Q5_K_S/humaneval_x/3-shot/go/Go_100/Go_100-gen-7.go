    result := make([]int, n)
    current := n

    for i := 0; i < len(result); i++ {
        result[i] = current
        if i%2==0 {
            current += 2
        }else {
            current += 1
        }
    }
    return result
}



