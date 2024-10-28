    result := make([]int, 0)
    if a % 2 == 0 {
        result = append(result, a)
    }
    for a+2 <= b {
        a += 2
        result = append(result, a)
    }
    if b % 2 == 0 {
        result = append(result, b)
    }
    return result
}



