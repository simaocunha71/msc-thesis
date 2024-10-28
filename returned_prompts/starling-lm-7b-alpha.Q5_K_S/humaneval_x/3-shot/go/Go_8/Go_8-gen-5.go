    result := [2]int{0,1}
    for _, n := range numbers {
        result[0] += n
        result[1] *= n
    }
    return result
}



