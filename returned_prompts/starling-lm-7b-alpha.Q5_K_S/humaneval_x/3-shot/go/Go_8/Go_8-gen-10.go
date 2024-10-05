    result := [2]int{0,1}
    for _, v := range numbers {
        result[0] += v
        result[1] *= v
    }
    return result
}



