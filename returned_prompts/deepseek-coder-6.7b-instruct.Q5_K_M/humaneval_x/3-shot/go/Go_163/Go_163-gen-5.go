    var start, stop int
    if a < b {
        start = a
        stop = b
    } else {
        start = b
        stop = a
    }

    result := make([]int, 0)
    for i := start; i <= stop; i++ {
        if i%2 == 0 {
            result = append(result, i)
        }
    }
    return result
}



