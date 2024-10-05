    result := make([]int, 0)

    if a % 2 == 0 {
        result = append(result, a)
    }
    if b % 2 == 0 {
        result = append(result, b)
    }
    for i := a + 1; i < b; i++ {
        if i % 2 == 0 {
            result = append(result, i)
        }
    }
    return result
}




