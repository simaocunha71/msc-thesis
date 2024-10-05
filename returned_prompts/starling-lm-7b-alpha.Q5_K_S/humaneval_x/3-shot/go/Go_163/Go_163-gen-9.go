    result := make([]int, 0)
    for a <= b {
        if a % 2 == 0 {
            result = append(result, a)
        }
        a++
    }
    return result
}




