    if a > b {
        a, b = b, a
    }
    var result []int
    for i := a; i <= b; i++ {
        if i%2 == 0 {
            result = append(result, i)
        }
    }
    return result
}



